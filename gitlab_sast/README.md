# GitLab SAST

GitLab SAST integrates into GitLab's Continuous Integration and leverages FLOSS scanning tools for the most common languages. For more information please see [Supported Languages and Frameworks](https://docs.gitlab.com/ee/user/application_security/sast/#supported-languages-and-frameworks). It then reads the results of those tools and creates a report in a common JSON format.

## Analyzer Data
It is important to note that these different tools do not leverage the same *properties* for their scanner output. For more information please see [Analyzers Data](https://docs.gitlab.com/ee/user/application_security/sast/analyzers.html#analyzers-data). 

### Additional Resources
* [GitLab Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
* [GitLab SAST Analyzers](https://docs.gitlab.com/ee/user/application_security/sast/analyzers.html)
