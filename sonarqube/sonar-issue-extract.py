#!/usr/bin/env python
import requests
import csv,sys
from pprint import pprint as pp
import argparse

# Retrieve token from user profile
# This works against the sonarqube 6.7.1 LTE version and sonarcloud.io
# Sample run:
# ./sonarapi.py --host http://localhost:9000 --key 6c6a5042a0e6a97959297c53f0fae99e10807e2c --output test.csv
# ./sonarapi.py --host https://sonarcloud.io --key XXXXXXXXXXXXXXXXba73fe3e67b42382e9240 --output test.csv --project barbich_django-DefectDojo
# 

def _url(path, url):
    return url + path

def get_security_issues(base_key=None,  url=None, componentKeys=None):
    issues=[]
    f_filter="types=VULNERABILITY&statuses=OPEN,CONFIRMED,REOPENED&componentKeys=%s"%componentKeys
    f_page=1
    while True:
        #print(_url('/api/issues/search?%s&additionalFields=_all&p=%i&ps=10' % (f_filter,f_page),  url))
        try:
            r=requests.get(_url('/api/issues/search?%s&additionalFields=_all&p=%i&ps=10' % (f_filter,f_page),  url),auth=(base_key, '')).json()
        except:
            print("Querying issues failed ...")
            raise
        for issue in r["issues"]:
            issues.append(issue)
        if r["paging"]["pageIndex"]*r["paging"]["pageSize"]>=r["paging"]["total"]:
            break
        else:
            f_page=f_page+1
        
    return issues

def get_rule(f_rule, base_key=None,  url=None):
	return requests.get(_url('/api/rules/show?key=%s' % (f_rule),  url),auth=(base_key, ''))

def get_projects(base_key=None,  url=None):
	return requests.get(_url('/api/components/search?qualifiers=TRK&ps=300',  url),auth=(base_key, ''))

def  get_languagedistribution(base_key=None,  url=None,  component=None):
    # /api/measures/component?qualifiers=TRK&component=barbich_django-DefectDojo&metricKeys=ncloc_language_distribution
    return requests.get(_url('/api/measures/component?qualifiers=TRK&component=%s&metricKeys=ncloc_language_distribution' % (component),  url),auth=(base_key, ''))

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host",type=str, help="host that runs sonarqube (http://acme.corp:9000)",  required=True )
    parser.add_argument("--key",type=str, help="access key",  required=True)
    parser.add_argument("--output",type=str, help="output csv file",  required=False)
    parser.add_argument("--language",type=str, help="language output csv file",  required=False)
    parser.add_argument("--project",type=str, help="filter on project ID(name) (if absent we will only list all projects)",  required=False,  action='append')
    parser.add_argument("--debug",action='store_true', help="debug",  required=False)
    args = parser.parse_args()
    # retrieve projects and associated information
    if not args.project:
        r= get_projects(base_key=args.key,  url=args.host).json()['components']
        projects={}
        components_a=[]
        components_ka=[]
        for project in r:
                projects[project['name']]={'name':project['name'],  'key':project['key']   }
                components_a.append(project['name'])
                components_ka.append(project['key'])
        components=','.join(components_a)
        componentKeys=','.join(components_ka)
        #print(projects)
        pp(projects)
        sys.exit(0)
    else:
        componentKeys=','.join(args.project)
        if args.debug: print("Debug: ", componentKeys)

    # retrieve issues for indicated project
    issues = get_security_issues(base_key=args.key,  url=args.host,  componentKeys=componentKeys)
    if args.debug: print("Debug: ", issues)
    
    # retrieve language distribution
    if args.project and args.language:
        csv_f=open(args.language, "wb")
        language_file=csv.writer(csv_f,  delimiter=';', escapechar="\\")
        language_file.writerow(['project', 'language', 'lines'])
        for p in args.project:
            languages = get_languagedistribution(base_key=args.key,  url=args.host,  component=p)
            if args.debug: print("Debug: ", languages.json()['component']['measures'])
            for m in languages.json()['component']['measures']:
                if m['metric'] == 'ncloc_language_distribution':
                    for l in m['value'].split(';'): language_file.writerow([p, l.split('=')[0], l.split('=')[1]])
        csv_f.close()

    
    if not args.output:
        pp(issues)
        sys.exit(0)
    
    csv_f=open(args.output, "wb")
    issues_file=csv.writer(csv_f,  delimiter=';', escapechar="\\")
    issues_file.writerow([
        'project', 
        'component', 
        'creationDate', 
        'updateDate', 
        'severity', 
        'status', 
        'key', 
        'langName', 
        'name', 
        'htmlDesc'])
    for issue in issues:
        vuln=get_rule(issue['rule'],  base_key=args.key,  url=args.host).json()['rule']
        issues_file.writerow([
            issue['project'], 
            issue['component'], 
            issue['creationDate'], 
            issue['updateDate'], 
            issue['severity'], 
            issue['status'], 
            vuln['key'], 
            vuln['langName'], 
            vuln['name'], 
            vuln['htmlDesc']])

    sys.exit(0)
