-ORT-


The OSS Review Toolkit (ORT) aims to assist with the tasks that commonly need to be performed in the context of license
compliance checks, especially for (but not limited to) Free and Open Source Software dependencies.

It does so by orchestrating a _highly customizable_ pipeline of tools that _abstract away_ the underlying services.
These tools are implemented as libraries (for programmatic use) and exposed via a command line interface (for scripted
use):

* [_Analyzer_](https://github.com/oss-review-toolkit/ort/blob/master/README.md#analyzer) - determines the dependencies of projects and their meta-data, abstracting which package
  managers or build systems are actually being used.
* [_Downloader_](https://github.com/oss-review-toolkit/ort/blob/master/README.md#downloader) - fetches all source code of the projects and their dependencies, abstracting which
  Version Control System (VCS) or other means are used to retrieve the source code.
* [_Scanner_](https://github.com/oss-review-toolkit/ort/blob/master/README.md#scanner) - uses configured source code scanners to detect license / copyright findings, abstracting
  the type of scanner.
* [_Evaluator_](https://github.com/oss-review-toolkit/ort/blob/master/README.md#evaluator) - evaluates license / copyright findings against customizable policy rules and license
  classifications.
* [_Reporter_](https://github.com/oss-review-toolkit/ort/blob/master/README.md#reporter) - presents results in various formats such as visual reports, Open Source notices or
  Bill-Of-Materials (BOMs) to easily identify dependencies, licenses, copyrights or policy rule violations.

The following tools are [planned](https://github.com/oss-review-toolkit/ort/projects/1) but not yet available:

* _Advisor_ - retrieves security advisories based on the Analyzer result.


DefectDojo provides an importer for the [Evaluated model reporter in JSON Format](./evaluated-model-reporter-output.json)