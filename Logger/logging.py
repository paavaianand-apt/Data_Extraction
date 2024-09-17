'''
This function is used to log the successes and exceptions
'''
from configparser import ConfigParser
from datetime import datetime

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

Log_files = config_object['LOG FILE DETAILS']
log_file_exceptions = open(Log_files["exceptions"], 'a', encoding = "utf-8")
log_file_success = open(Log_files["success"], 'a', encoding = "utf-8")
def start_logging():
    '''
    Function to open log files
    '''
    log_file_exceptions.write('\nSTART: ' + str(datetime.now()) + '\n')
    log_file_success.write('\nSTART: ' + str(datetime.now()) + '\n')

def write_exceptions(content):
    '''
    Function to write exceptions onto log file
    '''
    log_file_exceptions.write(content)

def write_success(content):
    '''
    Function to write success status onto log file
    '''
    log_file_success.write(content)

