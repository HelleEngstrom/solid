def validateUser(user, standardMessages):
    isUserValid = True

    if not user.firstname.isalpha():
        isUserValid = False
        standardMessages.printInvalidFieldMessage("förnamn")

    if not user.lastname.isalpha():
        isUserValid = False
        standardMessages.printInvalidFieldMessage("efternamn")

    if not user.favoriteNumber.isnumeric():
        isUserValid = False
        standardMessages.printInvalidFieldMessage("nummer")

    return isUserValid
