#Converts applicants to employees

from applicant import Applicant
from admin_applicant import AdminApplicant
from superUser_applicant import SuperUserApplicant


def run():

    applicants = [
        Applicant("Pippi", "Långstrump"),
        AdminApplicant("Harry", "Potter"),
        SuperUserApplicant("Uncle", "Bob")
        ]

    employees = []

    for i in range(0, len(applicants)):
        employees.append(applicants[i].createEmployee())

#TODO: snygga till outputen
    for i in range(0, len(employees)):
        print("Förnamn: " + employees[i].firstname,
              "Efternamn: " + employees[i].lastname,
              "Användarnamn: " + employees[i].username,
              "isAdmin: " + str(employees[i].isAdmin),
)


if __name__ == "__main__":
    run()
