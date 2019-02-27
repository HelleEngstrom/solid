#Prompts the user for input and creates a username from it.

def run():
    print("Följ instruktionerna nedan för att skapa ett användarnamn.")

    firstname = input("Förnamn: ")
    if not firstname.isalpha():
        print("Ogiltigt förnamn.")
        return

    lastname = input("Efternamn: ")
    if not lastname.isalpha():
        print("Ogiltigt efternamn.")
        return

    number = input("Ditt favoritnummer: ")
    if not number.isnumeric():
        print("Ogiltigt nummer.")
        return

    username = firstname[:3] + lastname[:3] + number
    print("Ditt användarnamn är " + username + ".")


if __name__ == "__main__":
    run()
