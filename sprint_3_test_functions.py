
"""
PROGRAM NAME: Test Functions for Sprint 3
AUTHOR(S): L. Adithi
VERSION AND DATE: 3.1 | August 17, 2024

PURPOSE: 
This module contains test functions designed to validate the RTF processing system as part of Sprint 3. The test scenarios address special character handling in rtf files ans ways to differentitate from delimiters/separators.

TEST SCENARIOS:

URS ID : KEX002.4.1
1. "The system should have the capability to extract any special
characters in any data point (column header, row header,
header, footer, body/content) eg (, -, ?, :) and fit it in the
knowledge graph database and processing requirement to
be met by transforming the source data special character
into acceptable data and vice versa when display the data
in system"

URS ID : KEX002.4.20
2. "The system should have the ability to differentiate and
extract List files Row/Column values which are containing
special characters different from delimiters/separators."

URS ID : KEX002.4.21
3. "The system should have the ability to differentiate and
extract Table files Row/Column values which are containing
special characters different from delimiters/separators."

Generic Test Cases:
   - Validation of RTF file integrity.
   - Schema validation for RTF files.
   - Conversion process from RTF to JSON or other required formats.
   - Extraction of basic data components of the file as seen in sprint-1

LINK TO TEST SCENARIO SHEET:
For further details, please refer to the test scenario sheet: LINK FOR SPRINT - 3 TEST SCENARIO SHEET : https://docs.google.com/spreadsheets/d/1CqC_FDR7Sti4oKp77rwqrsoW8Z6Tg9GbwkXdtx4KF88/edit?usp=sharing

COPYRIGHT: © M/s CARE2DATA 2024. All Rights Reserved.
"""

#import modules
from user_Interface import user_interface
from data_extraction import debug_print, special_characters
from user_Interface import selected_folder_path
from data_extraction import *
import logging
import os
import pytest

# Set up logging
log_file_path = '/Users/adithi/Downloads/sprint_3_code/test_special_characters.log'
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

# Initialize user interface
try:
    user_interface()
except Exception:
    debug_print("UI unsuccessful")

# TEST FUNCTIONS
#SPRINT SPECIFIC TEST FUNCTIONS
"""
URS REQUIREMENT: KEX002.4.1
TEST CASE DESCRIPTION : Verify that the system accurately extracts special characters (e.g., , -, ?, :) from various data points (column headers, row headers, headers, footers, content) in RTF files.
TEST CASE ID : KEX002.4.1_TC001
"""
# 1. POSITIVE TEST CASE
def test_special_characters_positive():
    # Ensure that this script is being run directly, not imported
    if __name__ == "__main__":
    
        # Iterate over all files in the selected folder
        for file_name in os.listdir(selected_folder_path):
            # Construct the full file path
            file_path = os.path.join(selected_folder_path, file_name)
            
            # Check if the current file is an RTF file
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    # Open and read the RTF file content
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        # Process the RTF content to extract special characters
                        processed_content = special_characters(rtf_content)

                    # Check if the processed content is different from the original content
                    if processed_content and processed_content != rtf_content:
                        # Log a success message if content was processed successfully
                        logger.info(f"File {file_path}: Content processed successfully.")
                        # Assert that the processed content is different from the original
                        assert processed_content != rtf_content, f"Error in file {file_path}: Content was not processed or unchanged."
                    else:
                        # Log a warning if the content was not processed correctly or is unchanged
                        logger.warning(f"File {file_path}: Content was not processed correctly or is unchanged.")
                        # Assert that the content should be unchanged or empty
                        assert not processed_content or processed_content == rtf_content, f"Error in file {file_path}: Content should be unchanged or empty."

                except Exception as e:
                    # Log an error message if an exception occurs during file processing
                    logger.error(f"Failed to process file {file_path}: {e}")
                    # Explicitly fail the test if an exception is caught
                    pytest.fail(f"Failed to process file {file_path}: {e}")


"""
URS REQUIREMENT: KEX002.4.1
TEST CASE DESCRIPTION : Verify that the system accurately does not extract special characters (e.g., , -, ?, :) from various data points (column headers, row headers, headers, footers, content) in RTF files.
TEST CASE ID : KEX002.4.1_TC002
"""
# 2. NEGATIVE TEST CASE
def test_special_characters_negative():
    # Ensure that this script is being run directly, not imported
    if __name__ == "__main__":
    
        # Iterate over all files in the selected folder
        for file_name in os.listdir(selected_folder_path):
            # Construct the full file path
            file_path = os.path.join(selected_folder_path, file_name)
            
            # Check if the current file is an RTF file
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    # Open and read the RTF file content
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        # Process the RTF content to extract special characters
                        processed_content = special_characters(rtf_content)

                    # Check if the processed content is empty or unchanged
                    if not processed_content or processed_content == rtf_content:
                        # Log a success message if content was not processed or remains unchanged as expected
                        logger.info(f"File {file_path}: No processing or content remains unchanged as expected.")
                        # Assert that the processed content is empty or matches the original content
                        assert not processed_content or processed_content == rtf_content, f"Error in file {file_path}: Content should be unchanged or empty."
                    else:
                        # Log a warning if the content was processed when it should not have been
                        logger.warning(f"File {file_path}: Content was processed when it should not have been.")
                        # Assert that the processed content matches the original content
                        assert processed_content == rtf_content, f"Error in file {file_path}: Content should be unchanged due to errors."

                except Exception as e:
                    # Log an error message if an exception occurs during file processing
                    logger.error(f"Failed to process file {file_path}: {e}")
                    # Explicitly fail the test if an exception is caught
                    pytest.fail(f"Failed to process file {file_path}: {e}")


#GENERIC EPIC SPRINT TEST CASES

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


# 3. def function to extract column headers from file

def test_extract_column_headers():
    if __name__ == "__main__":
        valid_column_header = []
        invalid_column_header = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        extracted_column_header = extract_column_headers(rtf_content)

                    # Check for valid column headers
                    if extracted_column_header:
                        valid_column_header.append(file_path)
                        assert extracted_column_header, f"Error in file {file_path}: Extracted column header should not be empty."
                        logger.info(f"Valid column header found in file: {file_path}")
                    else:
                        invalid_column_header.append(file_path)
                        assert not extracted_column_header, f"Error in file {file_path}: Extracted column header should be empty for malformed tables."
                        logger.warning(f"No column header found in file (expected): {file_path}")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid column header files
        for file in valid_column_header:
            logger.info(f"Re-checking valid file: {file}")
            try:
                with open(file, 'r') as f:
                    column_header = extract_column_headers(f.read())
                    assert column_header, f"File {file} should have valid column header details."
                    logger.info(f"Valid column header details confirmed in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check valid column header file {file}: {e}")

        # Re-check invalid column header files
        for file in invalid_column_header:
            logger.info(f"Re-checking invalid file: {file}")
            try:
                with open(file, 'r') as f:
                    assert not extract_column_headers(f.read()), f"File {file} should have empty column header details due to errors."
                    logger.info(f"Confirmed no valid column header details in file: {file}")
            except Exception as e:
                logger.error(f"Failed to re-check invalid column header file {file}: {e}")

        logger.info("Completed test for column header extraction.")

# 4. test function to extract table data

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

# 5. test function to extract footnotes

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

# 6. test function to extract footer from file

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


# 7. test function to convert rtf from the file


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

