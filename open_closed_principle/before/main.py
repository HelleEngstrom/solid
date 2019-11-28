#Converts applicants to employees

from applicant import Applicant
from employee_processor import createEmployee

def run():

    applicants = [
        Applicant("Pippi", "Långstrump"),
        Applicant("Harry", "Potter", True),
        Applicant("Uncle", "Bob")
        ]

    employees = []

    for i in range(0, len(applicants)):
        employees.append(createEmployee(applicants[i]))

    for i in range(0, len(employees)):
        print("Förnamn: " + employees[i].firstname, "Efternamn: " + employees[i].lastname, "Användarnamn: " + employees[i].username)


if __name__ == "__main__":
    run()
