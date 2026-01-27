import logging
import os
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')

def get_current_time():
    return datetime.now().strftime('%H:%M:%S')

def create_directory(path):
    try:
        os.mkdir(path)
        logging.info(f'Directory {path} created successfully')
    except OSError as e:
        logging.error(f'Error creating directory {path}: {e}')

def remove_directory(path):
    try:
        os.rmdir(path)
        logging.info(f'Directory {path} removed successfully')
    except OSError as e:
        logging.error(f'Error removing directory {path}: {e}')

def get_file_extension(filename):
    return os.path.splitext(filename)[1]

def get_filename_without_extension(filename):
    return os.path.splitext(filename)[0]

def is_file_empty(filename):
    return os.path.getsize(filename) == 0

class FileUtil:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            logging.error(f'File {self.filename} not found')
            return None

    def write_file(self, content):
        try:
            with open(self.filename, 'w') as file:
                file.write(content)
            logging.info(f'File {self.filename} written successfully')
        except Exception as e:
            logging.error(f'Error writing file {self.filename}: {e}')