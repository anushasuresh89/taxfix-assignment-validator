validator.py:
The validation logic is written in this file. This is the python file to be executed to validate the jsonl file of data. This must be invoked with a command line argument that specifies the file path of the input data.


config.py:
list_values: Has a known list of acceptable values to validate the fields against
patterns: Has the regex patterns which values must conform to
nullables:  Has a list of fields that is acceptable if it is null or missing


Expected output:
When validator.py is invoked, it generates two files upon a successful run - validator.log and report.json. The json file has the report for each event recorded in the input data file.