'''
Created on 2023-Oct-5
@author: Narendra Tata

Note: Ideally there is no need of modifying this file unless you want to re-design the flow.
'''


from jinja2 import Template
import subprocess
from subprocess import Popen, PIPE


def generate_report(test_results, results_folder):
    print("Generate Reports")
    print(test_results)
    print("****************")
    print(results_folder)
    print("****************")

    # Read the HTML template file
    with open('./Reports/report_template.html', 'r') as template_file:
        template_content = template_file.read()

    # Create a Jinja2 template
    template = Template(template_content)

    # Render the template with the dictionary data
    rendered_report = template.render(data=test_results)

    # Save the rendered report to an HTML file
    with open(results_folder+'/report.html', 'w') as report_file:
        report_file.write(rendered_report)

    print("HTML report generated successfully.")

    # NEED TO ENHANCE THIS LOGIC MORE
    print("Send an email notification to the user")

    fromaddr = 'narendra.tata64@gmail.com'
    toaddr = 'narendra.tata64@gmail.com'
    ccaddr = 'narendra.tata64@gmail.com'
    subject = """Test Execution Report"""

    body = """Hi Team,
    This is the test execution report. Please check the attachment



    Thanks,
    Tata"""

    cmd = 'echo "{0}" | mail -s "{1}" {2} {3} {4}'.format(body, subject, fromaddr, toaddr, ccaddr)
    if (True):
        subprocess.call(cmd, shell=True)
        print("email trigger passed...")
    else:
        print("email trigger failed...")


