from random_username.generate import generate_username

#Welcome User
def welcomeUser():
    print("\nWelcome to the text analysis tool, I will mine and analyze a body of text from a file you give me")

# Get Username
def getUsername():

    maxAttemps = 3
    attempts = 0

    while attempts < maxAttemps:

         # print mmessage prompting user to input their name
        inputPrompt = ""

        if attemps == 0:
        usernameFromInput = input("\nTo begin, please enter your username:\n") 
        else:
            inputPrompt = "\nPlease try again:\n
        usernameFromInput = input(inputPrompt)

        # validate username
        if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
            print("Your username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), have no space and cannot start with a number")
        else:
            return usernameFromInput

        attempts += 1

    print("Exhausted all " + str(maxAttemps) + " attemps, Assigning new username instead...")
    return generate_username()[0]


# Greet the User
def greetUser(name):
    print("Hello, " + name)

def runProgram():
    welcomeUser()
    username = getUsername()
    greetUser(username)

runProgram()