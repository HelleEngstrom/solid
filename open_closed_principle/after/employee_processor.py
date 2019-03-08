from employee import Employee

def createEmployee(applicant):
    employee = Employee(
        firstname = applicant.firstname,
        lastname = applicant.lastname,
        username = applicant.firstname[:3] + applicant.lastname[:3]
    )
    return employee

def createAdminEmployee(applicant):
    employee = Employee(
        firstname = applicant.firstname,
        lastname = applicant.lastname,
        username = applicant.firstname[0] + applicant.lastname
    )
    return employee


def createSuperUserEmployee(applicant):
    employee = Employee(
        firstname = applicant.firstname,
        lastname = applicant.lastname,
        username = applicant.firstname + applicant.lastname
    )
    return employee
