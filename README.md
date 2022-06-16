# splunk-msueberkrueb
Utility functions for creating importable log-files for splunk


## Installation Guide:

Write:
> git+https://github.com/msueberkrueb/msueberkrueb_splunk.git#egg=msueberkrueb_splunk

into the requirements.txt.

Run:
> pip install -r requirements.txt


## Config Guide:

### Import data options:

- "data_location": is the location of the needed key in the data dictionary
- "data_destination" (optional): is the location where the value from "data_location" should be placed
- "split" (optional): is used to split a value into n values on the specified delimiters. Syntax: "{"delimiters": [List, of, delimiters], "data_destinations": [List, of, destinations]]"