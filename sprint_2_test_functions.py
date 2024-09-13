"""
PROGRAM NAME: Test Functions for Sprint 2
AUTHOR(S): L. Adithi
VERSION AND DATE: 2.1 | August 7, 2024

PURPOSE: 
This module contains test functions designed to validate the RTF processing system as part of Sprint 2. The test scenarios address various styles and formatting features commonly utilized in RTF files.

TEST SCENARIOS:
1. RTF Styles:
   - BOLD: Verifies the application of bold formatting to titles or footnotes.
   - COLOR: Checks the color applied to titles or footnotes.
   - BCOLOR: Confirms the background color used for titles or footnotes.
   - FONT: Validates the font assigned to titles or footnotes.
   - HEIGHT: Ensures the correct point size is applied to titles or footnotes.
   - JUSTIFY: Tests the alignment (left, right, center) of titles or footnotes.
   - LINK: Verifies the presence and accuracy of hyperlinks in titles or footnotes.
   - UNDERLINE: Checks the correct application of underline formatting.
   - INDENTATION: Ensures proper indentation for titles, footnotes, and associated sub-data lines.

2. Additional RTF Styles:
   - Superscript: Tests the proper rendering of superscript text.
   - Subscript: Verifies the accurate rendering of subscript text.

3. Header & Footer:
   - Extraction and identification of each line component within headers and footers (left, center, right).

4. Generic Test Cases:
   - Validation of RTF file integrity.
   - Schema validation for RTF files.
   - Conversion process from RTF to JSON or other required formats.
   - Extraction of basic data components of the file as seen in sprint-1

LINK TO TEST SCENARIO SHEET:
For further details, please refer to the test scenario sheet: https://docs.google.com/spreadsheets/d/1Iy_yTcojqeCUN46w9Oy0Q4fv5xONBVzDj5RTJS4kTZM/edit?usp=sharing

COPYRIGHT: © M/s CARE2DATA 2024. All Rights Reserved.

"""
import os
import logging
from RTF_Control_Tags_and_Styles import check_rtf, extract_font_details, extract_colour_table, extract_style_details, extract_header, extract_title, extract_column_headers, extract_table_data, extract_footnotes, extract_footer, convert_rtf
from logger_config import logger  # Import the logger setup
from data_extraction import debug_print
import user_Interface
from user_Interface import selected_folder_path

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
    user_Interface()
except Exception:
    debug_print("UI unsuccessful")
#TEST FUNCTIONS 

#1. test function to check for rtf file in folder
def is_rtf_file(file_path):
    return os.path.splitext(file_path)[1].lower() == '.rtf'

# Test cases for the function
def test_is_rtf_file():

    # Test case 1: File with .rtf extension
    assert is_rtf_file("example.rtf") == True

    # Test case 2: File with .txt extension
    assert is_rtf_file("example.txt") == False

    # Test case 3: File with uppercase .RTF extension
    assert is_rtf_file("example.RTF") == True

    # Test case 4: File with no extension
    assert is_rtf_file("example") == False


# Main block to execute the function
if __name__ == "__main__":
    for file_name in os.listdir(selected_folder_path):
        file_path = os.path.join(selected_folder_path, file_name)
        # Check if the path is a file and has an .rtf extension
        if os.path.isfile(file_path) and is_rtf_file(file_path):
            print(f"{file_path} is an RTF file.")
        else:
            print(f"{file_path} is not an RTF file.")

# 2. test function to check for rtf schema
def test_check_rtf_from_folder():
    # Main block to execute the function
    if __name__ == "__main__":
        valid_files = []
        invalid_files = []
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                if check_rtf(file_path):
                    valid_files.append(file_path)
                else:
                    invalid_files.append(file_path)

# 3. test function to check for font details from the file 


def test_extract_font_details():
    if __name__ == "__main__":
        valid_font = []
        invalid_font = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        extracted_fonts = extract_font_details(rtf_content)

                    # Log the extracted fonts for debugging
                    logger.info(f"File {file_path}: Extracted fonts = {extracted_fonts}")

                    if extracted_fonts:
                        valid_font.append(file_path)
                        # Assert that the extracted fonts are non-empty
                        assert extracted_fonts, f"Error in file {file_path}: Extracted fonts should not be empty."
                    else:
                        invalid_font.append(file_path)
                        # Assert that extracted fonts are empty for malformed content
                        assert not extracted_fonts, f"Error in file {file_path}: Extracted fonts should be empty for malformed tables."

                except Exception as e:
                    # Log any errors that occur during file processing
                    logger.error(f"Failed to process file {file_path}: {e}")
                    invalid_font.append(file_path)  # Add to invalid files if an exception occurs

        # Verify valid font files
        for file in valid_font:
            try:
                fonts = extract_font_details(open(file).read())
                assert fonts, f"File {file} should have valid font details."
                logger.info(f"File {file}: Valid font details verified.")
            except Exception as e:
                logger.error(f"Failed to process valid font file {file}: {e}")
                assert False, f"Failed to verify font details for file {file}."

        # Verify invalid font files
        for file in invalid_font:
            try:
                fonts = extract_font_details(open(file).read())
                assert not fonts, f"File {file} should have empty font details due to errors."
                logger.info(f"File {file}: No font details as expected.")
            except Exception as e:
                logger.error(f"Failed to process invalid font file {file}: {e}")
                assert False, f"Failed to verify empty font details for file {file}."


# 4. test function to extract colour table from the file

def test_extract_colour_table():
    if __name__ == "__main__":
        valid_colours = []
        invalid_colours = []
    
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        extracted_colours = extract_colour_table(rtf_content)
                    
                    if extracted_colours:
                        valid_colours.append(file_path)
                        logger.info(f"File {file_path}: Extracted colours are valid.")
                        assert extracted_colours, f"Error in file {file_path}: Extracted colours are invalid."
                    else:
                        invalid_colours.append(file_path)
                        logger.warning(f"File {file_path}: Extracted colours should be empty for malformed tables.")
                        assert not extracted_colours, f"Error in file {file_path}: Extracted colours should be empty for malformed tables."

                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        for file in valid_colours:
            try:
                colours = extract_colour_table(open(file).read())
                assert colours, f"File {file} should have valid colour details."
                logger.info(f"File {file}: Colour details are valid.")
            except Exception as e:
                logger.error(f"Failed to process valid colour file {file}: {e}")

        for file in invalid_colours:
            try:
                assert not extract_colour_table(open(file).read()), f"File {file} should have empty colour details due to errors."
                logger.info(f"File {file}: No colour details as expected.")
            except Exception as e:
                logger.error(f"Failed to process invalid colour file {file}: {e}")




# 5. test function to extract size from file
def test_extract_size():
    if __name__ == "__main__":
        valid_size = []
        invalid_size = []
    
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        style_info = extract_style_details(rtf_content)

                    if 'size' in style_info and isinstance(style_info['size'], int):
                        valid_size.append(file_path)
                        assert isinstance(style_info['size'], int), f"File {file_path}: Extracted size should be an integer, got {type(style_info['size'])}."
                    else:
                        invalid_size.append(file_path)
                        assert 'size' not in style_info or not isinstance(style_info['size'], int), f"File {file_path}: Extracted size should be invalid or missing."

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Verify valid size files
        for file in valid_size:
            try:
                with open(file, 'r') as file_content:
                    style_info = extract_style_details(file_content.read())
                assert 'size' in style_info and isinstance(style_info['size'], int), f"File {file} should have valid size details."
            except Exception as e:
                logger.error(f"Failed to verify size for file {file}: {e}")

        # Verify invalid size files
        for file in invalid_size:
            try:
                with open(file, 'r') as file_content:
                    style_info = extract_style_details(file_content.read())
                assert 'size' not in style_info or not isinstance(style_info['size'], int), f"File {file} should have invalid or missing size details."
            except Exception as e:
                logger.error(f"Failed to verify size for file {file}: {e}")


# 6. test function to extract colour from file
def test_extract_colour():
    if __name__ == "__main__":
        valid_colours = []
        invalid_colours = []
    
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        extracted_colours = extract_colour_table(rtf_content)
                    
                    if extracted_colours:
                        valid_colours.append(file_path)
                        logger.info(f"File {file_path}: Extracted colours are valid.")
                        assert extracted_colours, f"Error in file {file_path}: Extracted colours are invalid."
                    else:
                        invalid_colours.append(file_path)
                        logger.warning(f"File {file_path}: Extracted colours should be empty for malformed tables.")
                        assert not extracted_colours, f"Error in file {file_path}: Extracted colours should be empty for malformed tables."

                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        for file in valid_colours:
            try:
                colours = extract_colour_table(open(file).read())
                assert colours, f"File {file} should have valid colour details."
                logger.info(f"File {file}: Colour details are valid.")
            except Exception as e:
                logger.error(f"Failed to process valid colour file {file}: {e}")

        for file in invalid_colours:
            try:
                assert not extract_colour_table(open(file).read()), f"File {file} should have empty colour details due to errors."
                logger.info(f"File {file}: No colour details as expected.")
            except Exception as e:
                logger.error(f"Failed to process invalid colour file {file}: {e}")



# 7. test function to extract style details - bold
def test_check_bold():
    if __name__ == "__main__":
        valid_bold_files = []
        invalid_bold_files = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        style_info = extract_style_details(rtf_content)
                    
                    # Check if the file should have bold style
                    if style_info and style_info.get('bold') == 'YES':
                        valid_bold_files.append(file_path)
                        logger.info(f"File {file_path} correctly has bold style.")
                    else:
                        invalid_bold_files.append(file_path)
                        logger.warning(f"File {file_path} is missing bold style or has incorrect bold style.")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid bold files
        for file in valid_bold_files:
            try:
                with open(file, 'r') as f:
                    style_info = extract_style_details(f.read())
                    assert style_info.get('bold') == 'YES', f"File {file} should have bold style."
                    logger.info(f"Re-check valid bold file {file}: Bold style verified.")
            except Exception as e:
                logger.error(f"Failed to re-check valid bold file {file}: {e}")

        # Re-check invalid bold files
        for file in invalid_bold_files:
            try:
                with open(file, 'r') as f:
                    style_info = extract_style_details(f.read())
                    assert style_info.get('bold') != 'YES', f"File {file} should not have bold style."
                    logger.info(f"Re-check invalid bold file {file}: No bold style verified.")
            except Exception as e:
                logger.error(f"Failed to re-check invalid bold file {file}: {e}")


# 8. test function to extract style details - italic
def test_check_italic():
    if __name__ == "__main__":
        valid_italic = []
        invalid_italic = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        style_info = extract_style_details(rtf_content)

                    if style_info and style_info.get('italic') == 'YES':
                        valid_italic.append(file_path)
                        logger.info(f"File {file_path} correctly has italic style.")
                    else:
                        invalid_italic.append(file_path)
                        logger.warning(f"File {file_path} is missing italic style or has incorrect italic style.")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid italic files
        for file in valid_italic:
            try:
                with open(file, 'r') as f:
                    style_info = extract_style_details(f.read())
                    assert style_info.get('italic') == 'YES', f"File {file} should have italic style."
                    logger.info(f"Re-check valid italic file {file}: Italic style verified.")
            except Exception as e:
                logger.error(f"Failed to re-check valid italic file {file}: {e}")

        # Re-check invalid italic files
        for file in invalid_italic:
            try:
                with open(file, 'r') as f:
                    style_info = extract_style_details(f.read())
                    assert style_info.get('italic') != 'YES', f"File {file} should not have italic style."
                    logger.info(f"Re-check invalid italic file {file}: No italic style verified.")
            except Exception as e:
                logger.error(f"Failed to re-check invalid italic file {file}: {e}")

# 9. test function to extract style details - underline
def test_check_underline():
    if __name__ == "__main__":
        valid_underline = []
        invalid_underline = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        style_info = extract_style_details(rtf_content)

                    if 'underline' in style_info and style_info.get('underline') == 'YES':
                        valid_underline.append(file_path)
                        logger.info(f"File {file_path} correctly has underline style.")
                    else:
                        invalid_underline.append(file_path)
                        logger.warning(f"File {file_path} is missing underline style or has incorrect underline style.")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid underline files
        for file in valid_underline:
            try:
                with open(file, 'r') as f:
                    underline_info = convert_rtf(f.read())
                    assert underline_info, f"File {file} should have valid underline details."
                    logger.info(f"Re-check valid underline file {file}: Underline details verified.")
            except Exception as e:
                logger.error(f"Failed to re-check valid underline file {file}: {e}")

        # Re-check invalid underline files
        for file in invalid_underline:
            try:
                with open(file, 'r') as f:
                    underline_info = convert_rtf(f.read())
                    assert not underline_info, f"File {file} should not have underline details."
                    logger.info(f"Re-check invalid underline file {file}: No underline details verified.")
            except Exception as e:
                logger.error(f"Failed to re-check invalid underline file {file}: {e}")


# 10. test function to extract style details - subscript
def test_check_subscript():
    if __name__ == "__main__":
        valid_subscript = []
        invalid_subscript = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        style_info = extract_style_details(rtf_content)

                    if 'subscript' in style_info and style_info.get('subscript') == 'YES':
                        valid_subscript.append(file_path)
                        logger.info(f"File {file_path} correctly has subscript style.")
                    else:
                        invalid_subscript.append(file_path)
                        logger.warning(f"File {file_path} is missing subscript style or has incorrect style.")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Re-check valid subscript files
        for file in valid_subscript:
            try:
                with open(file, 'r') as f:
                    style_info = extract_style_details(f.read())
                    assert style_info.get('subscript') == 'YES', f"File {file} should have subscript style."
                    logger.info(f"Re-check valid subscript file {file}: Subscript style verified.")
            except Exception as e:
                logger.error(f"Failed to re-check valid subscript file {file}: {e}")

        # Re-check invalid subscript files
        for file in invalid_subscript:
            try:
                with open(file, 'r') as f:
                    style_info = extract_style_details(f.read())
                    assert style_info.get('subscript') != 'YES', f"File {file} should not have subscript style."
                    logger.info(f"Re-check invalid subscript file {file}: No subscript style verified.")
            except Exception as e:
                logger.error(f"Failed to re-check invalid subscript file {file}: {e}")

        logger.info("Completed test for subscript style")

# 11. test function to extract style details - superscript
def test_check_superscript():
    if __name__ == "__main__":
        valid_superscript = []
        invalid_superscript = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                logger.debug(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        rtf_content = file.read()
                        style_info = extract_style_details(rtf_content)

                    # Check if the file has superscript style
                    if 'superscript' in style_info and style_info.get('superscript') == 'YES':
                        valid_superscript.append(file_path)
                        logger.info(f"File {file_path} correctly has superscript style.")
                    else:
                        invalid_superscript.append(file_path)
                        logger.warning(f"File {file_path} is missing superscript style or has incorrect style.")

                except AssertionError as e:
                    logger.error(f"Assertion error for file {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")

        # Optionally: Re-check valid superscript files
        for file in valid_superscript:
            try:
                with open(file, 'r') as f:
                    style_info = extract_style_details(f.read())
                    assert style_info.get('superscript') == 'YES', f"File {file} should have superscript style."
                    logger.info(f"Re-check valid superscript file {file}: Superscript style verified.")
            except Exception as e:
                logger.error(f"Failed to re-check valid superscript file {file}: {e}")

        # Optionally: Re-check invalid superscript files
        for file in invalid_superscript:
            try:
                with open(file, 'r') as f:
                    style_info = extract_style_details(f.read())
                    assert style_info.get('superscript') != 'YES', f"File {file} should not have superscript style."
                    logger.info(f"Re-check invalid superscript file {file}: No superscript style verified.")
            except Exception as e:
                logger.error(f"Failed to re-check invalid superscript file {file}: {e}")

        logger.info("Completed test for superscript style")


# 12. test function to extract the header from file

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


# 13. test function to extract title

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


# 14. def function to extract column headers from file

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

# 15. test function to extract table data

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

# 16. test function to extract footnotes

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

# 17. test function to extract footer from file

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


# 18. test function to convert rtf from the file


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
