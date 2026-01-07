from random_username.generate import generate_username

#Welcome User
def welcomeUser():
    print("\nWelcome to the text analysis tool, I will mine and analyze a body of text from a file you give me")

# Get Username
def getUsername():
    # print mmessage prompting user to input their name
    usernameFromInput = input("\nTo begin, please enter your username:\n")

    if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
        print("Your username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), have no space and cannot start with a number")
        usernameFromInput = generate_username()[0]
        print("Assigning new username instead...")

    return usernameFromInput

# Greet the User
def greetUser(name):
    print("Hello, " + name)

def runProgram():
    welcomeUser()
    username = getUsername()
    greetUser(username)

runProgram()