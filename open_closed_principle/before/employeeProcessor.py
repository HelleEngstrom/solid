from Employee import Employee

def createEmployee(applicant):
    employee = Employee(
        firstname = applicant.firstname,
        lastname = applicant.lastname,
        username = applicant.firstname[:3] + applicant.lastname[:3]
    )
    return employee
