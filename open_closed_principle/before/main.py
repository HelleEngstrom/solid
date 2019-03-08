#Converts applicants to employees

from applicant import Applicant
from employee_processor import createEmployee

def run():

    applicants = [
        Applicant("Pippi", "Långstrump"),
        Applicant("Harry", "Potter"),
        Applicant("Uncle", "Bob")
        ]

    employees = []

    for i in range(0, len(applicants)):
        employees.append(createEmployee(applicants[i]))

    for i in range(0, len(employees)):
        print(employees[i].firstname, employees[i].lastname, employees[i].username)


if __name__ == "__main__":
    run()
