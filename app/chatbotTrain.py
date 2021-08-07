import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
import random
import nltk
from nltk.stem import WordNetLemmatizer
import yaml
import pickle

lemmatizer = WordNetLemmatizer()
words = []
classes = []
documents = []
ignoreLetters = ['!', '?', ',', '.']
intentsFile = open('chatbot.model/intents.yaml').read()
intents = yaml.safe_load(intentsFile)

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenization of the intents
        word = nltk.word_tokenize(pattern)
        # put them into a list
        words.extend(word)
        # add intents with a tag to documents
        documents.append((word, intent['tag']))
        # add tags to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lemmaztize words, lower letters, remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignoreLetters]
words = sorted(list(set(words)))

# documents - patterns and tags
print(len(documents), "documents")
print(documents)
# classes = tags
classes = sorted(list(set(classes)))
print(len(classes), "classes")
print(classes)
# words = all words
print(len(words), "unique words")
print(words)

# serialize words
wordsFile = open('chatbot.model/words.pkl', 'wb')
pickle.dump(words, wordsFile)
wordsFile.close()
# serialize classes
classesFile = open('chatbot.model/classes.pkl', 'wb')
pickle.dump(classes, classesFile)
classesFile.close()

# training data
training = []
# empty array for our output
outputEmpty = [0] * len(classes)

# create training set
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    patternWords = doc[0]
    # lemmatize each word again to get patterns
    patternWords = [lemmatizer.lemmatize(word.lower()) for word in patternWords]
    # create our bag of words array with 1, if word match found in current pattern
    for word in words:
        bag.append(1) if word in patternWords else bag.append(0)

    # output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(outputEmpty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training, dtype=object)

# create train and test lists. x - patterns, y - intents
trainX = list(training[:, 0])
trainY = list(training[:, 1])
print("Training data created")

# 3 layers - 1st layer 128 neurons, 2nd layer 64 neurons, 3rd output layer - number of neurons equal to number of
# intents to predict output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(trainX[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(trainY[0]), activation='softmax'))

# stochastic gradient descent with Nesterov accelerated gradient
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# fitting and saving the model
hist = model.fit(np.array(trainX), np.array(trainY), epochs=200, batch_size=5, verbose=1)
model.save('chatbot.model/chatbotModel.h5', hist)

print("model created")
