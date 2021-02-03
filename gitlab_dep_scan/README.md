# GitLab Dependency Scanning

GitLab Dependency Scanning integrates into GitLab's Continuous Integration and leverages FLOSS scanning tools to automatically find security vulnerabilities in dependencies. For more information please see [supported languages and package managers](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/#supported-languages-and-package-managers). It then reads the results of those tools and creates a report in a common JSON format.

## Analyzer Data
It is important to note that these different tools do not leverage the same *properties* for their scanner output. For more information please see [analyzers data](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/analyzers.html#analyzers-data).

### Additional Resources
* [GitLab Dependency Scanning](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/)
* [GitLab Dependency Scanning Analyzers](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/analyzers.html)
