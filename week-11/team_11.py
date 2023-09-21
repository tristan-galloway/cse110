"""
Author: Unathletic Avengers
Teacher: Brother Keers
File: team_11.py
Assignment: write a program to iterate through each line of this file, gather the information from each field and display or take certain actions depending on the data.

"""

# Set indexes so if they change later it's easier to change all locations in the code
NAME_INDEX = 0
ID_INDEX = 1
JOB_INDEX = 2
SAL_INDEX = 3

#Open the hr_system.txt and store it as a variable name hr_file
with open("hr_system.txt", "r") as hr_file:
 
    # Read each of the lines in and sepperates each column into different variables  
    for line in hr_file:
        # Use the spaces as the seperation point for the columns
        column = line.split(" ")

        # Correcting formatting by removing blank space with .strip()
        # Make thee name, id, job, and salary comlumns
        employee_name = column[NAME_INDEX].strip()
        employee_id = column[ID_INDEX].strip()
        employee_job = column[JOB_INDEX].strip()
        employee_sal = int(column[SAL_INDEX].strip()) / 24

        # Give an extra 1000 dollars to Engineers
        if employee_job == "Engineer":
            employee_sal = employee_sal + 1000

        # Print the list of Employees with their ID, Job title, and bi-weekly paycheck
        print(f"{employee_name} (ID: {employee_id}), {employee_job} - ${employee_sal:,.2f}")