#Welcome User
def welcomeUser():
    print("\nWelcome to the text analysis tool, I will mine and analyze a body of text from a file you give me")

# Get Username
def getUsername():
    # print mmessage prompting user to input their name
    usernameFromInput = input("\nTo begin, please enter your username:\n")
    return usernameFromInput

# Greet the User
def greetUser(name):
    print("Hello, " + name)

def runProgram():
    welcomeUser()
    username = getUsername()
    greetUser(username)

runProgram()