from employee_processor import createEmployee

class Applicant:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def createEmployee(self):
        employee = createEmployee(self)
        return employee
