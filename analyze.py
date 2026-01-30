from random_username.generate import generate_username

import re, nltk, json
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('vader_lexicon')
wordLemmatizer = WordNetLemmatizer()
stopWords = set(stopwords.words('english'))
sentimentAnalyzer = SentimentIntensityAnalyzer()


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

# Convert part of speech from pos_tag() function into woordnet compactable pos text
posToWordnetTag =  {
    "J": wordnet.ADJ,
    "V": wordnet.VERB,
    "N": wordnet.NOUN,
    "R": wordnet.ADV
}

def treebankPosToWordnetPos(partOfSpeech):
    posFirstChar = partOfSpeech[0]
    if posFirstChar in posToWordnetTag:
        return posToWordnetTag[posFirstChar]
    return wordnet.NOUN


# Convert raw list of (word, POS) tuple to a list strings that only include valid english words
def cleanseWordList(posTaggedWordTuples):
    cleanseWords = []
    invalidWordPattern = "[^a-zA-Z-+]"
    for posTaggedWordTuple in posTaggedWordTuples:
        word = posTaggedWordTuple[0]
        pos = posTaggedWordTuple[1]
        cleanseWord = word.replace(".", "").lower()
        if (not re.search(invalidWordPattern, cleanseWord)) and len(cleanseWord) > 1 and cleanseWord not in stopWords:
            cleanseWords.append(wordLemmatizer.lemmatize(cleanseWord, treebankPosToWordnetPos(pos)))
    return cleanseWords

# Get User Details
welcomeUser()
username = getUsername()
greetUser(username)

# Extract and Tokenize Text
articleTextRaw = getArticleText()
articleSentences = tokenizeSentences(articleTextRaw)
articleWords = tokenizeWords(articleSentences)

# Get Sentence Analytics
stockSearchPattern = "[0-9]|[%$€£]|thousand|billion|million|trillion|profit|loss"
keySentences = extractKeySentences(articleSentences, stockSearchPattern)
wordsPerSentence = getWordsPerSentence(articleSentences)

# Get Word Analytics
wordsPosTagged = nltk.pos_tag(articleWords)
articleWordsCleansed = cleanseWordList(wordsPosTagged)

# Generate word cloud
separator = " "
wordCloudFilePath = "results/wordcloud.png"
wordcloud = WordCloud(width = 1000, height = 700, random_state=1, \
 background_color= "salmon", colormap= "Pastel1", collocations=False).generate(separator.join(articleWordsCleansed))
wordcloud.to_file(wordCloudFilePath)

# Run Sentiment Analysis
sentimentResult = sentimentAnalyzer.polarity_scores(articleTextRaw)

# Collate Analyses into one dictionary
finalResult = {
    "username": username,
    "data": {
        "keySentences": keySentences,
        "wordsPerSentence": wordsPerSentence,
        "sentiment": sentimentResult,
        "wordCloudFilePath": wordCloudFilePath
    },
    "metadata": {
        "snetencesAnalyzed": len(articleSentences),
        "wordsAnalyzed": len(articleWordsCleansed)
    }
}

finalResultJson = json.dumps(finalResult, indent=4)

# Print for testing
print(finalResultJson)