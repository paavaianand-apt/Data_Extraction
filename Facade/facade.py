'''
* PROGRAM NAME: RTF TO JSON CONVERTOR
* VERSION AND DATE: 2.0 09-08-2024
* AUTHOR NAME(s): Shreeja Katama

* LANGUAGE AND LIBRARY REFERENCE: Python3,
Python Standard Libraries:
  - json
  - re
  - os
  - tkinter
  - configparser
  - datetime

* PURPOSE: Processes RTF files to extract basic data and convert it to JSON format. 
Includes dynamic extraction using control words and robust error handling.
* PARAMETERS: Folder containing RTF files as an input parameter.
* RETURNS: JSON outputs saved in a new directory.
* FUNCTION CALL NAME(s): rtf_to_json
* FUNCTION PURPOSE: Extracts data from RTF files and converts it to JSON format.
* EMBEDDED PROGRAMS: None
* MODULE: rtf_to_json.py

* COPY RIGHT: M/s CARE2DATA 2024  All Rights Reserved
**************************************************************************

* VERSION HISTORY

* REVISED VERSION AND DATE: 1.0.0 01-07-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Initial Version

* REVISED VERSION AND DATE: 1.2.0 07-07-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Integration of UI with the code

* REVISED VERSION AND DATE: 1.3.0 16-07-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Dynamic Approach for extraction

* REVISED VERSION AND DATE: 1.4.0 30-07-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Split the code into functional blocks

* REVISED VERSION AND DATE: 1.5.0 06-08-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Implementation of Sprint 1 Demo Corrections

* REVISED VERSION AND DATE: 2.0.0 09-08-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Implementation of Sprint 2

* REVISED VERSION AND DATE: 3.0.0 18-08-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Implementation of Sprint 3 and Sprint 2 Corrections
'''
from configparser import ConfigParser
from UI.user_Interface import user_interface

from DataExtraction.data_extraction import debug_print
from Logger import logging1

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

# Get the RTF tags, RE expressions and alignment data from the config file
Debug_flag = config_object["DEBUG FLAG"]
RTF_tags = config_object["RTF TAGS"]
RE_expressions = config_object["RE EXPRESSIONS"]
Header_alignment = config_object['HEADER ALIGNMENT']
Log_files = config_object['LOG FILE DETAILS']
RTF_Style_Tags = config_object['RTF STYLE TAGS']

try:
    user_interface(logging1.write_exceptions, RTF_tags)

except ImportError as e: #pragma nocover
    debug_print("UI unsuccessful") #pragma nocover
