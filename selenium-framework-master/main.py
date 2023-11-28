'''
Created on 2023-Oct-5
@author: Narendra Tata

Note: Ideally there is no need of modifying this file unless you want to re-design the flow.
Code execution should be started from this file
'''


from selenium_framework.common import *
from Execution.test_run import *
from Reports.generate_report import *


prt(0, 'Testing Starts on %s' % getFormatedCurrentTime())
# Testing Start ----------------------------------
test_results = {}
test_results_tuple = test_run()
# Unpack the tuple into individual variables
test_results, results_folder = test_results_tuple

generate_report(test_results, results_folder)
# Testing End ------------------------------------
prt(0, 'Testing Finished on %s' % getFormatedCurrentTime())
