class Employee:
    def __init__(self, firstname, lastname, username, isAdmin=False, isSuperuser=False):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.isAdmin = isAdmin
        self.isSuperuser = isSuperuser
