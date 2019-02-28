from employeeProcessor import createSuperUserEmployee

class SuperuserApplicant:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.isAdmin = True
        self.isSuperuser = True

    def createEmployee(self):
        employee = createSuperUserEmployee(self)
        return employee
