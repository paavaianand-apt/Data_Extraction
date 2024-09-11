'''
This module is used to create the json object for each RTF file
'''
import json
import os
from datetime import datetime

def json_conversion(json_dictionary, item, output_directory, write_success):
    '''
    Function to create json file
    '''
    output_file = os.path.join(
        output_directory,
        f"{os.path.splitext(os.path.basename(item))[0]}.json"
        )
    def write_json_success(content):
        write_success(content)
    with open(output_file, 'w', encoding = "utf-8") as f:
        json.dump(json_dictionary , f, ensure_ascii=False, indent=4)
    write_json_success(datetime.now().isoformat() + f" Data successfully written to {output_file}\n")

    return "Successful", ""
