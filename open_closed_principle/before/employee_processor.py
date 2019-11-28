from employee import Employee

def createEmployee(applicant):
    if applicant.isAdmin:
        username = applicant.firstname[0] + applicant.lastname
    else:
        username = applicant.firstname[:3] + applicant.lastname[:3]

    employee = Employee(
        firstname = applicant.firstname,
        lastname = applicant.lastname,
        username = username
    )
    return employee
