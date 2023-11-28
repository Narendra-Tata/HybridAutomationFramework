'''
Created on 2023-Nov-5
@author: Narendra Tata

Note: Just import your testcases file in this file. no other modifications needed.

Make sure Execution/TestCases.xls had all the testcases same as the testcase method names in test_cases.py
'''


from AUT.ATGFR8.test_cases import *
import pandas as pd
import os
import datetime
from Reports.results_folders import *


def test_run():
    test_results = {}
    results_directory = "./AUT/ATGFR8/Results"
    # Load the Test Cases Excel file into a DataFrame
    df = pd.read_excel('./Execution/TestCases.xls')

    # Filter rows where 'Execute' is 'y' and select the 'TestCase' column
    test_cases_to_execute = df[df['Execute'] == 'y']['TestCase'].tolist()

    # Print the list of test cases to execute
    print(test_cases_to_execute)

    # Create the run specific result folder under project repo
    results_folder_name = create_results_folders(results_directory)

    # Call the test cases one by one and capture the result
    for testcase_name in test_cases_to_execute:
        try:
            # Use eval() to call the function by its name
            result = eval(testcase_name + '()')
            # Assign the result to the dictionary with the test case name as the key
            test_results[testcase_name] = result

        except NameError:
            print(f"Function {testcase_name} not found")

    return test_results, results_folder_name

