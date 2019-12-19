-Fortify-

Micro Focus Fortify Static Code Analyzer reduces software risk by identifying security vulnerabilities that pose the biggest threats to your organization. It pinpoints the root cause of the vulnerability, correlates and prioritizes results, and provides best practices so developers can develop code more securely.

Website: https://www.microfocus.com/en-us/products/static-code-analysis-sast/how-it-works

## Creating Fortify XML Reports for Import to Defect Dojo

A Fortify XML file is created from the fortify .fpr file

Note a .fpr file is a .zip file with a collection of files in it.

The reportgenerator utility can be used to generate an XML file from the FPR file:

```C:\Program Files\HPE_Security\Fortify_SCA_and_Apps_17.20\bin\ReportGenerator.bat -format XML -f fortify_v18.20.1046.xml -source fortify_v18.20.1046.fpr```

The above method will get you just one representative issue from each type of issue (&lt;GroupingSection&gt;) .
In order to import all issues you need to jump through a couple of hoops 

```cd %FORTIFY_HOME%/Core/config/reports```

Copy the DefaultReportDefinition.xml to DefaultReportDefinitionAllIssues.xml

Change

```<IssueListing limit="1" listing="true">```

To:

```<IssueListing limit="-1" listing="true">```

  
Change:

```<Refinement>[fortify priority order]:critical OR [fortify priority order]:high</Refinement>```

To:

```<Refinement/>```

The reportgenerator utility can be used to generate an XML file from the FPR file, specifying the new template file:

```C:\Program Files\HPE_Security\Fortify_SCA_and_Apps_17.20\bin\ReportGenerator.bat -template DefaultReportDefinitionAllIssues.xml -format XML -f fortify_v18.20.1046.xml -source fortify_v18.20.1046.fpr```
