import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import random
import yaml

from dataFunctions import *

lemmatizer = WordNetLemmatizer()
model = load_model('chatbot.model/chatbotModel.h5')
intents = yaml.safe_load(open('chatbot.model/intents.yaml').read())
words = pickle.load(open('chatbot.model/words.pkl', 'rb'))
classes = pickle.load(open('chatbot.model/classes.pkl', 'rb'))


# text preprocessing
def cleanUpSentence(sentence):
    # split words into array
    sentenceWords = nltk.word_tokenize(sentence)
    # stem every word
    sentenceWords = [lemmatizer.lemmatize(word.lower()) for word in sentenceWords]
    return sentenceWords


def bagOfWords(sentence, show_details=True):
    # tokenize the patterns
    sentenceWords = cleanUpSentence(sentence)
    # create a zero-padded array with the length of the list of words
    bag = [0] * len(words)

    for s in sentenceWords:
        for i, word in enumerate(words):
            if word == s:
                # set 1 if word exists in a sentence
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % word)

    # return bag of words array
    return np.array(bag)


def predictClass(sentence):
    # filter words that exists in the sentence
    bag = bagOfWords(sentence, show_details=False)
    # predict bag array using our trained model
    res = model.predict(np.array([bag]))[0]

    # set largest allowable error value
    errorThreshold = 0.25
    # make an array with values where error is smaller than threshold error
    results = [[i, r] for i, r in enumerate(res) if r > errorThreshold]

    # sort strength probability
    results.sort(key=lambda x: x[1], reverse=True)
    returnList = []
    for r in results:
        returnList.append({"intent": classes[r[0]], "probability": str(r[1])})
    return returnList


def getResponse(ints, intentsYaml):
    # get the tag
    tag = ints[0]['intent']

    # read the file
    listOfIntents = intentsYaml['intents']

    for i in listOfIntents:
        # look for the tag in the file
        if i['tag'] == tag:
            # get random response
            result = random.choice(i['responses'])

            # check the context
            if i['context'] == ['saveMoodData']:
                # check if date exists
                if checkIfDateExists():
                    result = "I'm sorry. I have just checked and I have already recorded your mood for today!"
                else:
                    # save data
                    saveMoodData(tag)

            return result
