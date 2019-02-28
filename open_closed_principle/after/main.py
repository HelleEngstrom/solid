#Converts applicants to employees

from Applicant import Applicant
from AdminApplicant import AdminApplicant
from SuperuserApplicant import SuperuserApplicant

def run():

    applicants = [
        Applicant("Pippi", "Långstrump"),
        AdminApplicant("Harry", "Potter"),
        SuperuserApplicant("Uncle", "Bob")
        ]

    employees = []

    for i in range(0, len(applicants)):
        employees.append(applicants[i].createEmployee())
    
    for i in range(0, len(employees)):
        print(employees[i].firstname, employees[i].lastname, employees[i].username)


if __name__ == "__main__":
    run()
