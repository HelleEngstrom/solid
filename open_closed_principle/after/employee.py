#Här skulle vi kunna dela upp employee i flera filer precis som applicant. Men vi har ingen logik här, så vi väljer att inte göra det.

class Employee:
    def __init__(self, firstname, lastname, username, isAdmin = False, isSuperUser = False):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.isAdmin = isAdmin
        self.isSuperUser = isSuperUser
