"""
CSV Preprocessing and Data Restructuring Module
================================================

This module provides utilities to preprocess a CSV file, segregate its content into smoke testing
and regression testing sections, and restructure the data into key-value pairs for further analysis.

Functions
---------
1. preprocess_file(file_path):
    - Reads a CSV file and segregates its lines into `smoke_testing` and `regression_testing` sections.
    - Skips irrelevant lines, such as blank lines and extra headers.

2. read_csv(file_path):
    - Uses `preprocess_file` to clean and segregate the CSV data.
    - Restructures the data in each section into a list of dictionaries for easy access.

3. restructure_to_key_value_pair(input):
    - Converts a list of CSV lines into a structured list of dictionaries.
    - Uses the header row as keys and subsequent rows as values.

Usage
-----
This module is designed to process a CSV file with mixed content (e.g., smoke test and regression data),
clean the input, and provide structured output for testing or reporting purposes.

Example:
--------
Suppose we have a CSV file (`example.csv`) with the following content:

"""
import csv

def preprocess_file(file_path):
    """
    Preprocess a CSV file to extract and segregate lines into smoke testing and regression testing sections.

    The function reads a file line by line, identifies sections based on specific keywords, and skips unwanted lines
    (such as empty lines or header-like rows). It categorizes lines into two groups: `smoke_testing` and `regression_testing`.

    Args:
        file_path (str): The path to the CSV file to be processed.

    Returns:
        dict: A dictionary containing two keys:
            - 'smoke_testing': List of lines belonging to the smoke testing section.
            - 'regression_testing': List of lines belonging to the regression testing section.
    
    Notes:
        - Lines starting with `,,,,,` or containing "Tester" are ignored.
        - The first line of the file is added to both `smoke_testing` and `regression_testing` sections as a header.
        - The function uses the keywords 'Smoke Test Data' and 'Regression,,,,,' to identify section boundaries.

    Example:
        Input file:
        ```
        Header Line
        Smoke Test Data
        Line 1
        Regression,,,,,
        Line 2
        ```
        Output:
        {
            'smoke_testing': ['Header Line', 'Smoke Test Data', 'Line 1'],
            'regression_testing': ['Header Line', 'Line 2']
        }
    """
    cleaned_lines = {'smoke_testing':[],'regression_testing':[]}
    smoke_testing = False
    regression_testing = False
    with open(file_path, mode='r',encoding='UTF-8') as file:
        for index, line in enumerate(file):
            line.strip()
            if index == 0:
                cleaned_lines['smoke_testing'].append(line)
                cleaned_lines['regression_testing'].append(line)
            if 'Smoke Test Data' in line:
                smoke_testing = True
                continue
            if 'Regression,,,,,' in line:
                smoke_testing = False
                regression_testing = True
                continue
            if line[0:5] == ',,,,,' or line[0:6] == 'Tester':
                continue
            if smoke_testing is True:
                cleaned_lines['smoke_testing'].append(line)
            elif regression_testing is True:
                cleaned_lines['regression_testing'].append(line)
    return cleaned_lines

def read_csv(file_path):
    """
    Reads a CSV file, preprocesses its content, and restructures it into a dictionary of key-value pairs
    for smoke testing and regression testing sections.

    This function uses `preprocess_file` to clean and segregate the file's lines into `smoke_testing` and
    `regression_testing` sections. It then restructures the data in each section into key-value pairs using
    the `restructure_to_key_value_pair` function.

    Args:
        file_path (str): The path to the CSV file to be read and processed.

    Returns:
        dict: A dictionary containing two keys:
            - 'smoke_testing': A list of dictionaries, each representing a key-value pair of the smoke testing data.
            - 'regression_testing': A list of dictionaries, each representing a key-value pair of the regression testing data.
        
        If no data exists for a particular section, the value will be an empty list.

    Dependencies:
        - `preprocess_file(file_path)`: Used to clean and segregate raw file content.
        - `restructure_to_key_value_pair(data)`: Used to convert raw section data into structured dictionaries.

    Example:
        Input File (simplified for clarity):
        ```
        Header Line
        Smoke Test Data
        Name, Age, Status
        John, 30, Active
        Regression,,,,,
        Name, Age, Status
        Jane, 25, Inactive
        ```

        Output:
        {
            'smoke_testing': [
                {'Name': 'John', 'Age': '30', 'Status': 'Active'}
            ],
            'regression_testing': [
                {'Name': 'Jane', 'Age': '25', 'Status': 'Inactive'}
            ]
        }
    """
    cleaned_lines_dict = preprocess_file(file_path)
    data = {'smoke_testing':[],'regression_testing':[]}
    smoke_data = cleaned_lines_dict.get('smoke_testing')
    if smoke_data is not None:
        data['smoke_testing'] = restructure_to_key_value_pair(smoke_data)
    regression_data = cleaned_lines_dict.get('regression_testing')
    if regression_data is not None:
        data['regression_testing'] = restructure_to_key_value_pair(regression_data)
    return data
        
        
        
def restructure_to_key_value_pair(input_list:list):
    """
    Converts a list of CSV lines into a structured list of dictionaries with key-value pairs.

    This function uses `csv.DictReader` to parse CSV input data and generate dictionaries
    where the keys are derived from the header row and the values are from subsequent rows.

    Args:
        input (list of str): A list of lines representing a CSV, including a header row followed by data rows.

    Returns:
        list of dict: A list of dictionaries, where each dictionary corresponds to a row of data.
                      Keys are derived from the header row, and values are the corresponding cell values.

    Example:
        Input:
        [
            "Name,Age,Status",
            "John,30,Active",
            "Jane,25,Inactive"
        ]

        Output:
        [
            {'Name': 'John', 'Age': '30', 'Status': 'Active'},
            {'Name': 'Jane', 'Age': '25', 'Status': 'Inactive'}
        ]

    Notes:
        - The `input` list must include a header row as the first element.
        - Blank lines in the input are ignored by `csv.DictReader`.
        - Ensure that the `input` lines are properly formatted as CSV data.

    Dependencies:
        - `csv.DictReader`: Used to parse the CSV data into dictionaries.
    """
    data = []
    reader = csv.DictReader(input_list)
    for row in reader:
        data.append(row)
    return data
            
            
            

print(read_csv('.\data\Test Data for Eploy-Sufa Testing(Australia).csv'))