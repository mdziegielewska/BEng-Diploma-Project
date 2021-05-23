import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random

from tkinter import *
import settings
import charts

model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# lemmatization - grouping together the different inflected forms of a word
# so they can be analysed as a single item
lemmatizer = WordNetLemmatizer()


def clean_up_sentence(sentence):
    # splitting words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stemming every word - reducing to base form
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for words that exist in sentence
def bag_of_words(sentence, show_details=True):
    # tokenizing patterns
    sentence_words = clean_up_sentence(sentence)
    # bag of words - vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % word)
    return np.array(bag)


def predict_class(sentence):
    # filter below threshold predictions
    p = bag_of_words(sentence, show_details=False)
    res = model.predict(np.array([p]))[0]
    error_treshold = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > error_treshold]
    # sorting strength probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


# tkinter chat gui
class Chat(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(width=450, height=600, bg="#f3f3cc")

        self.common_img = PhotoImage(width=1, height=1)  # in pixels

        # menu
        self.settings_button = Button(self, text="Settings", font=("Helvetica", 10), fg="#005b4b",
                                      image=self.common_img, width=141, height=32, bg="#ffffff", borderwidth=2,
                                      relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                      activebackground="#cac669", compound='c',
                                      command=lambda: master.show_frame(settings.Settings)).place(x=9, y=13)

        self.chat_button = Button(self, text="Chat", font=("Helvetica", 10), fg="#005b4b", image=self.common_img,
                                  width=141, height=32, bg="#cac669", borderwidth=2, relief=FLAT,
                                  highlightcolor="#005b4b", highlightbackground="#005b4b", activebackground="#cac669",
                                  compound='c', command=lambda: master.show_frame(Chat)).place(x=150, y=13)

        self.charts_button = Button(self, text="Charts", font=("Helvetica", 10), fg="#005b4b",
                                    image=self.common_img, width=141, height=32, bg="#ffffff", borderwidth=2,
                                    relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                    activebackground="#cac669", compound='c',
                                    command=lambda: master.show_frame(charts.Charts)).place(x=291, y=13)

        self.chat_box = Text(self, bg="#f3f3cc", font=("Helvetica", 10), fg="#005b4b", relief=FLAT, width=59,
                             height=26, wrap=WORD)
        self.chat_box.place(x=9, y=65, width=420, height=450)
        self.chat_box.config(state=DISABLED)

        self.scrollbar = Scrollbar(self, command=self.chat_box.yview)
        self.scrollbar.place(x=422, y=65, height=450)
        self.chat_box['yscrollcommand'] = self.scrollbar.set

        self.entry_box = Text(self, bg="white", font=("Helvetica", 10), fg="#005b4b", relief=FLAT)
        self.entry_box.place(x=158, y=525, width=280, height=59)

        self.send_button = Button(self, text="Send", font=("Helvetica", 10), fg="#005b4b", image=self.common_img,
                                  width=141, height=51, bg="#ffffff", borderwidth=2, relief=FLAT,
                                  highlightcolor="#005b4b", highlightbackground="#005b4b", activebackground="#cac669",
                                  compound='c', command=self.send_message).place(x=9, y=525)

    def send_message(self):
        msg = self.entry_box.get("1.0", 'end-1c').strip()
        self.entry_box.delete("0.0", END)

        if msg != '':
            self.chat_box.config(state=NORMAL)
            self.chat_box.insert(END, "You: " + msg + '\n\n')
            self.chat_box.config(foreground="#446665", font=("Helvetica", 10))

            ints = predict_class(msg)
            res = get_response(ints, intents)

            self.chat_box.insert(END, "Bot: " + res + '\n\n')

            self.chat_box.config(state=DISABLED)
            self.chat_box.yview(END)
