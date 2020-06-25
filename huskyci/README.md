-huskyCI-

huskyCI is an open source tool that orchestrates security tests and centralizes all results into a database for further analysis and metrics. It can perform static security analysis in Python ([Bandit][Bandit] and [Safety][Safety]), Ruby ([Brakeman][Brakeman]), JavaScript ([Npm Audit][NpmAudit] and [Yarn Audit][YarnAudit]), Golang ([Gosec][Gosec]), Java ([SpotBugs][SpotBugs] plus [Find Sec Bugs][FindSec]), and HCL ([TFSec][TFSec]). It can also audit repositories for secrets like AWS Secret Keys, Private SSH Keys, and many others using [GitLeaks][Gitleaks].

Github: https://github.com/globocom/huskyCI


[Bandit]: https://github.com/PyCQA/bandit
[Safety]: https://github.com/pyupio/safety
[Brakeman]: https://github.com/presidentbeef/brakeman
[Gosec]: https://github.com/securego/gosec
[NpmAudit]: https://docs.npmjs.com/cli/audit
[YarnAudit]: https://yarnpkg.com/lang/en/docs/cli/audit/
[Gitleaks]: https://github.com/zricethezav/gitleaks
[SpotBugs]: https://spotbugs.github.io
[FindSec]: https://find-sec-bugs.github.io
[TFSec]: https://github.com/liamg/tfsec