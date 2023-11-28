'''
Created on 2023-Oct-5
@author: Narendra Tata

Note: Ideally there is no need of modifying this file unless you want to re-design the flow.

This file will create the test results folder under project repository
'''


import os
import datetime


def create_results_folders(results_directory):
    print("Creating the results folders for test run")

    # Create a folder for the current test results
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Format the datetime as a string (e.g., "2023-09-14_150812" for September 14, 2023, at 3:08:12 PM)
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H%M%S")

    # Create a folder with the formatted datetime as its name to store the results
    results_folder_name = os.path.join(results_directory, formatted_datetime)
    screenshots = os.path.join(results_folder_name, 'screenshots')

    # Check if the folder already exists; if not, create it
    if not os.path.exists(results_folder_name):
        os.makedirs(results_folder_name)

    print(f"Created folder: {results_folder_name}")

    if not os.path.exists(screenshots):
        os.makedirs(screenshots)

    print(f"Created folder: {screenshots}")

    return results_folder_name
