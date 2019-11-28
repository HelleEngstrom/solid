from employee_processor import createSuperUserEmployee

class SuperUserApplicant:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.isAdmin = True
        self.isSuperUser = True

    def createEmployee(self):
        employee = createSuperUserEmployee(self)
        return employee
