from random_username.generate import generate_username
from nltk.tokenize import word_tokenize, sent_tokenize
import re

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

        if attempts == 0:
            usernameFromInput = input("\nTo begin, please enter your username:\n") 
        else:
            inputPrompt = "\nPlease try again:\n"
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


# Get text from file
def getArticleText():
    f = open("files/article.txt", "r")
    rawText = f.read()
    f.close()
    return rawText.replace("\n", " ").replace("\r", "")

# Extract Sentences from raw Text body
def tokenizeSentences(rawText):
    return sent_tokenize(rawText)

# Extract words from list of sentences
def tokenizeWords(sentences):
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))
    return words

# Get the key sentences based on search pattern of key words
def extractKeySentences(sentences, searchPattern):
    matchedSentences = []
    for sentence in sentences:
        # If sentence matches desired pattern, add to matchedSentences
        if re.search(searchPattern, sentence.lower()):
            matchedSentences.append(sentence)
    return matchedSentences

# Get the avarage word per sentence, excluding puctuation
def getWordsPerSentence(sentences):
    totalWords = 0
    for sentence in sentences:
        totalWords += len(sentence.split(" "))
    return totalWords / len(sentences)

# Get User Details
welcomeUser()
username = getUsername()
greetUser(username)

# Extract and Tokenize Text
articleTextRaw = getArticleText()
articleSentences = tokenizeSentences(articleTextRaw)
articleWords = tokenizeWords(articleSentences)

# Get Analytics
stockSearchPattern = "[0-9]|[%$€£]|thousand|billion|million|trillion|profit|loss"
keySentences = extractKeySentences(articleSentences, stockSearchPattern)
wordsPerSentence = getWordsPerSentence(articleSentences)

# Print for testing
print("GOT: ")
print(wordsPerSentence)


# for sentence in articleSentences:
#     print(sentence + "\n")