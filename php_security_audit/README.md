# Sample Scan Files

Sample scan files using Wordpress 4.9.8 <i>twentyseventeen</i> theme files.

PHP Security Audit outputs an optimized JSON file, included and named with suffix <i>_unformatted.json</i>.

There is no security vulnerabilities in <i>twentyseventeen</i> theme, so we introduced one in <i>index.php</i> by echoing out <code>$_GET['data']</code> with any validation or sanitization.

## Getting Started

Upload the sample file to the folder of the scanner. If the scanner folder is not there then please create it with the submission. The file should be in the format, <scanner_name>\_v<x.x>.ext

### Notice

Please do not upload any production data as the scan files are intended to be scrubbed or against demo systems.
