from User import User

def captureUserData():
    firstname = input("Förnamn: ")
    lastname = input("Efternamn: ")
    favoriteNumber = input("Ditt favoritnummer: ")

    user = User(firstname, lastname, favoriteNumber)
    return user

def createUsername(user):
    username = user.firstname[:3] + user.lastname[:3] + user.favoriteNumber
    return username
