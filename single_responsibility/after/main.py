#Prompts the user for input and creates a username from it.

from userHelper import captureUserData, createUsername
from StandardMessages import StandardMessages
from User import User
from validator import validateUser


def run():
    #setup
    standardMessages = StandardMessages()

    standardMessages.printWelcomeMessage()

    user = captureUserData()

    isUserValid = validateUser(user, standardMessages)

    if not isUserValid:
        return

    username = createUsername(user)

    standardMessages.printUsernameMessage(username)

if __name__ == "__main__":
    run()
