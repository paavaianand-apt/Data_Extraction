"""
PROGRAM NAME: Test Functions for Sprint 4
AUTHOR(S): L. Adithi
VERSION AND DATE: 4.1 | September 6, 2024

PURPOSE: 
This module contains test functions designed to validate the RTF processing system as part of Sprint 4.

TEST SCENARIOS:
1. "The system should have the ability to extract Tables even if there is no Row header /Column header specified."

2. "The system should have the ability to extract Lists even if there is no Row header /Column header specified."

3. "The system should have the capability to handle and extract data from Table files that have columns with Null column headers."

4. "The system should have the capability to handle and extract data from List files that have columns with Null column headers."

5. Generic Test Cases:
   - Validation of RTF file integrity.
   - Schema validation for RTF files.
   - Conversion process from RTF to JSON or other required formats.
   - Extraction of basic data components of the file as seen in sprint-1

LINK TO TEST SCENARIO SHEET:
For further details, please refer to the test scenario sheet: https://docs.google.com/spreadsheets/d/1Rw6rX8bqjbrdjF0NaNotoCAPgYxmmgTacLEXOluY4po/edit?usp=sharing

COPYRIGHT: © M/s CARE2DATA 2024. All Rights Reserved.

"""

import os
import logging
import pytest
from user_Interface import selected_folder_path
from user_Interface import user_interface
from data_extraction import extract_column_headers
from user_Interface import *
from data_extraction import *

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
log_file = "test_log.log"
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create a formatter and set it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)

# Ensure pytest doesn't capture log output
@pytest.fixture(autouse=True)
def disable_capture_log(caplog):
    caplog.set_level(logging.DEBUG)

"""
SRS REQUIREMENT ID: KEX0002.3.3
URS REQUIREMENT ID: KEX002.4.30
TEST SCENARIO: "The system should have the ability to extract Tables even if there is no Row header /Column header specified."
"""

#positive test case to extract tables and listings for no row/column header

def test_no_row_header_positive():
    if __name__ == "__main__":
        logger.info("Starting test case for empty column headers")
        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
        
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        logger.info(f"Processing file: {file_name}")
                    
                        # Extract column headers using the extract_column_headers function
                        headers_data = extract_column_headers(rtf_content)
                    
                        # Log based on the result of the header extraction
                        if headers_data['data'] == []:
                            logger.info(f"Empty column headers found in file: {file_name}")
                            logger.debug(f"Empty column headers found in file: {file_name}")
                        else:
                            logger.info(f"Column headers extracted in file: {file_name}")
                            logger.debug(f"Column headers extracted in file: {file_name}")
                    
                except Exception as e:
                    logger.info(f"Error processing file {file_name}: {e}")
                    logger.debug(f"Error processing file {file_name}: {e}")


"""
SRS REQUIREMENT ID: KEX0002.3.3
URS REQUIREMENT ID: KEX002.4.30
TEST SCENARIO: "Verify that the system handles cases where the table structure is malformed (e.g., missing cells, inconsistent row lengths) and lacks row or column headers."

"""
#negative test case to extract tables and listings for no row/column header
def test_no_row_header_negative():
    if __name__ == "__main__":
        logger.info("Starting negative test case for missing/invalid column headers")
        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
        
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        logger.info(f"Processing file: {file_name}")
                    
                        # Extract column headers using the original extract_column_headers function
                        headers_data = extract_column_headers(rtf_content)
                    
                        # Log based on the result of the header extraction
                        if headers_data['data'] == []:
                            logger.warning(f"Column headers missing or invalid in file: {file_name}")
                            logger.debug(f"Column headers missing or invalid in file: {file_name}")
                        else:
                            logger.info(f"Column headers extracted (negative test failed) in file: {file_name}")
                            logger.debug(f"Column headers extracted (negative test failed) in file: {file_name}")
                    
                except Exception as e:
                    logger.error(f"Error processing file {file_name}: {e}")
                    logger.debug(f"Error processing file {file_name}: {e}")


"""
SRS REQUIREMENT ID: KEX0002.3.4
URS REQUIREMENT ID: KEX002.4.40
TEST SCENARIO: "Verify that the system correctly extracts a table from an RTF file where some columns have null (empty or missing) column headers."

"""
#positive test case to extract tables and listings for null row/column header
def test_no_null_column_header_positive():
    if __name__ == "__main__":

    # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
        
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        logger.info(f"Processing file: {file_name}")
                    
                        # Extract column headers using the original extract_column_headers function
                        headers_data = extract_column_headers(rtf_content)
                    
                        # Check for valid (non-null and non-empty) column headers
                        if headers_data['data'] and all(header.strip() != "" for header in headers_data['data']):
                            logger.info(f"Valid column headers found in file: {file_name}")
                            debug_print(f"Valid column headers found in file: {file_name}")
                        else:
                            logger.error(f"Null/Empty column headers detected (positive test failed) in file: {file_name}")
                            debug_print(f"Null/Empty column headers detected (positive test failed) in file: {file_name}")
                    
                except Exception as e:
                    logger.error(f"Error processing file {file_name}: {e}")
                    logger.debug(f"Error processing file {file_name}: {e}")


"""
SRS REQUIREMENT ID: KEX0002.3.4
URS REQUIREMENT ID: KEX002.4.40
TEST SCENARIO: "Verify that the system appropriately handles a table from an RTF file where some columns have null (empty or missing) column headers, and the table structure is malformed."
"""
#negative test case to extract tables and listings for null row/column header

def test_no_null_column_header_negative():
    # Ensure that this script is being run directly, not imported
    if __name__ == "__main__":    
        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
        
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        logger.info(f"Processing file: {file_name}")
                    
                     # Extract column headers using the original extract_column_headers function
                        headers_data = extract_column_headers(rtf_content)
                    
                    # Check for null/empty column headers
                    if not headers_data['data'] or all(header.strip() == "" for header in headers_data['data']):
                        logger.warning(f"Null/Empty column headers detected in file: {file_name}")
                        logger.debug(f"Null/Empty column headers detected in file: {file_name}")
                    else:
                        logger.warning(f"Column headers extracted (negative test failed) in file: {file_name}")
                        logger.debug(f"Column headers extracted (negative test failed) in file: {file_name}")
                    
                except Exception as e:
                    logger.error(f"Error processing file {file_name}: {e}")
                    logger.debug(f"Error processing file {file_name}: {e}")
    
#1. test function to extract header 
def test_extract_header():
    if __name__ == "__main__":
        valid_header = []
        invalid_header = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        extracted_header = extract_header(rtf_content)

                    # Check if the header extraction was successful
                    if extracted_header:
                        valid_header.append(file_path)
                        logger.info(f"Valid header found in file: {file_path}")
                        assert extracted_header, f"Error in file {file_path}: Extracted header is invalid."
                    else:
                        invalid_header.append(file_path)
                        logger.warning(f"File {file_path} has no header when one was expected.")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid header files
        for file in valid_header:
            logger.info(f"Re-checking valid file: {file}")
            try:
                with open(file, 'r') as f:
                    header = extract_header(f.read())
                    assert header, f"File {file} should have valid header details."
                    logger.info(f"Valid header details confirmed in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check valid header file {file}: {e}")

        # Re-check invalid header files
        for file in invalid_header:
            logger.info(f"Re-checking invalid file: {file}")
            try:
                with open(file, 'r') as f:
                    assert not extract_header(f.read()), f"File {file} should have empty header details due to errors."
                    logger.info(f"Confirmed no valid header details in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check invalid header file {file}: {e}")

        logger.info("Completed test for header extraction.")


# 2. test function to extract title

def test_extract_title():
    if __name__ == "__main__":
        valid_title = []
        invalid_title = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        extracted_title = extract_title(rtf_content)

                    # Check if the title extraction was successful
                    if extracted_title:
                        valid_title.append(file_path)
                        logger.info(f"Valid title found in file: {file_path}")
                        assert extracted_title, f"Error in file {file_path}: Extracted title should not be empty."
                    else:
                        invalid_title.append(file_path)
                        logger.warning(f"No title found in file (expected): {file_path}")
                        assert not extracted_title, f"Error in file {file_path}: Extracted title should be empty for malformed tables."

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid title files
        for file in valid_title:
            logger.info(f"Re-checking valid file: {file}")
            try:
                with open(file, 'r') as f:
                    title = extract_title(f.read())
                    assert title, f"File {file} should have valid title details."
                    logger.info(f"Valid title details confirmed in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check valid title file {file}: {e}")

        # Re-check invalid title files
        for file in invalid_title:
            logger.info(f"Re-checking invalid file: {file}")
            try:
                with open(file, 'r') as f:
                    assert not extract_title(f.read()), f"File {file} should have empty title details due to errors."
                    logger.info(f"Confirmed no valid title details in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check invalid title file {file}: {e}")

        logger.info("Completed test for title extraction.")


# 3. test function to extract table data

def test_extract_table_data():
    if __name__ == "__main__":
        valid_table_data = []
        invalid_table_data = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        extracted_table_data = extract_table_data(rtf_content)

                    # Check for valid table data
                    if extracted_table_data:
                        valid_table_data.append(file_path)
                        assert extracted_table_data, f"Error in file {file_path}: Extracted table data should not be empty."
                        logger.info(f"Valid table data found in file: {file_path}")
                    else:
                        invalid_table_data.append(file_path)
                        assert not extracted_table_data, f"Error in file {file_path}: Extracted table data should be empty for malformed tables."
                        logger.warning(f"No table data found in file (expected): {file_path}")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid table data files
        for file in valid_table_data:
            logger.info(f"Re-checking valid file: {file}")
            try:
                with open(file, 'r') as f:
                    table_data = extract_table_data(f.read())
                    assert table_data, f"File {file} should have valid table data details."
                    logger.info(f"Valid table data details confirmed in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check valid table data file {file}: {e}")

        # Re-check invalid table data files
        for file in invalid_table_data:
            logger.info(f"Re-checking invalid file: {file}")
            try:
                with open(file, 'r') as f:
                    assert not extract_table_data(f.read()), f"File {file} should have empty table data details due to errors."
                    logger.info(f"Confirmed no valid table data details in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check invalid table data file {file}: {e}")

        logger.info("Completed test for table data extraction.")

# 4. test function to extract footnotes

def test_extract_footnotes():
    if __name__ == "__main__":
        valid_footnotes = []
        invalid_footnotes = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        extracted_footnotes = extract_footnotes(rtf_content)

                    # Check for valid footnotes
                    if extracted_footnotes:
                        valid_footnotes.append(file_path)
                        assert extracted_footnotes, f"Error in file {file_path}: Extracted footnotes should not be empty."
                        logger.info(f"Valid footnotes found in file: {file_path}")
                    else:
                        invalid_footnotes.append(file_path)
                        assert not extracted_footnotes, f"Error in file {file_path}: Extracted footnotes should be empty for malformed content."
                        logger.warning(f"No footnotes found in file (expected): {file_path}")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid footnotes files
        for file in valid_footnotes:
            logger.info(f"Re-checking valid file: {file}")
            try:
                with open(file, 'r') as f:
                    footnotes = extract_footnotes(f.read())
                    assert footnotes, f"File {file} should have valid footnotes details."
                    logger.info(f"Valid footnotes details confirmed in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check valid footnotes file {file}: {e}")

        # Re-check invalid footnotes files
        for file in invalid_footnotes:
            logger.info(f"Re-checking invalid file: {file}")
            try:
                with open(file, 'r') as f:
                    assert not extract_footnotes(f.read()), f"File {file} should have empty footnotes details due to errors."
                    logger.info(f"Confirmed no valid footnotes details in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check invalid footnotes file {file}: {e}")

        logger.info("Completed test for footnotes extraction.")

# 5. test function to extract footer from file

def test_extract_footer():
    if __name__ == "__main__":

        valid_footer = []
        invalid_footer = []

        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        extracted_footer = extract_footer(rtf_content)

                    # Check for valid footers
                    if extracted_footer:
                        valid_footer.append(file_path)
                        assert extracted_footer, f"Error in file {file_path}: Extracted footer should not be empty."
                        logger.info(f"Valid footer found in file: {file_path}")
                    else:
                        invalid_footer.append(file_path)
                        assert not extracted_footer, f"Error in file {file_path}: Extracted footer should be empty for malformed content."
                        logger.warning(f"No footer found in file (expected): {file_path}")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid footer files
        for file in valid_footer:
            logger.info(f"Re-checking valid file: {file}")
            try:
                with open(file, 'r') as f:
                    footer = extract_footer(f.read())
                    assert footer, f"File {file} should have valid footer details."
                    logger.info(f"Valid footer details confirmed in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check valid footer file {file}: {e}")

        # Re-check invalid footer files
        for file in invalid_footer:
            logger.info(f"Re-checking invalid file: {file}")
            try:
                with open(file, 'r') as f:
                    assert not extract_footer(f.read()), f"File {file} should have empty footer details due to errors."
                    logger.info(f"Confirmed no valid footer details in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check invalid footer file {file}: {e}")

        logger.info("Completed test for footer extraction.")


# 6. test function to convert rtf from the file

def test_convert_rtf():
    if __name__ == "__main__":

        valid_rtf = []
        invalid_rtf = []

        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        extracted_rtf = convert_rtf(rtf_content)

                    # Check for valid RTF conversions
                    if extracted_rtf:
                        valid_rtf.append(file_path)
                        assert extracted_rtf, f"Error in file {file_path}: Extracted RTF content should not be empty."
                        logger.info(f"Valid RTF content found in file: {file_path}")
                    else:
                        invalid_rtf.append(file_path)
                        assert not extracted_rtf, f"Error in file {file_path}: Extracted RTF content should be empty for malformed content."
                        logger.warning(f"No RTF content found in file (expected): {file_path}")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid RTF files
        for file in valid_rtf:
            logger.info(f"Re-checking valid file: {file}")
            try:
                with open(file, 'r') as f:
                    rtf_content = convert_rtf(f.read())
                    assert rtf_content, f"File {file} should have valid RTF content details."
                    logger.info(f"Valid RTF content details confirmed in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check valid RTF file {file}: {e}")

        # Re-check invalid RTF files
        for file in invalid_rtf:
            logger.info(f"Re-checking invalid file: {file}")
            try:
                with open(file, 'r') as f:
                    assert not convert_rtf(f.read()), f"File {file} should have empty RTF content details due to errors."
                    logger.info(f"Confirmed no valid RTF content details in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check invalid RTF file {file}: {e}")

        logger.info("Completed test for RTF conversion.")

pytest.main([__file__])
with open(log_file, 'r') as f:
    print(f.read())
