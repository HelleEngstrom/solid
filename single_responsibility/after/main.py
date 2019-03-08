#Prompts the user for input and creates a username from it.

from user_helper import captureUserData, createUsername
import standard_messages as standardMessages
from user import User
from validator import validateUser


def run():

    standardMessages.printWelcomeMessage()

    user = captureUserData()

    isUserValid = validateUser(user, standardMessages)

    if not isUserValid:
        return

    username = createUsername(user)

    standardMessages.printUsernameMessage(username)

if __name__ == "__main__":
    run()
