from employeeProcessor import createAdminEmployee

class AdminApplicant:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.isAdmin = True

    def createEmployee(self):
        employee = createAdminEmployee(self)
        return employee
