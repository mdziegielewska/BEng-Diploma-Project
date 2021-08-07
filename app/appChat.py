from tkinter import *

from chatbotConversation import *
from dataFunctions import *
from dataSecurity import *

import appSettings as settings
import appCharts as charts


# FRAME CLASS WITH CHAT
class Chat(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(width=450, height=600, bg="#f3f3cc")
        # to have a better control of the size of elements
        self.common_img = PhotoImage(width=1, height=1)  # in pixels

        # menu
        self.settingsButton = Button(self, text="Settings", font=("Helvetica", 10), fg="#005b4b",
                                     image=self.common_img, width=141, height=32, bg="#ffffff", borderwidth=2,
                                     relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                     activebackground="#cac669", compound='c',
                                     command=lambda: master.showFrame(settings.Settings)).place(x=9, y=13)

        self.chatButton = Button(self, text="Chat", font=("Helvetica", 10), fg="#005b4b", image=self.common_img,
                                 width=141, height=32, bg="#cac669", borderwidth=2, relief=FLAT,
                                 highlightcolor="#005b4b", highlightbackground="#005b4b", activebackground="#cac669",
                                 compound='c').place(x=150, y=13)

        self.chartsButton = Button(self, text="Charts", font=("Helvetica", 10), fg="#005b4b",
                                   image=self.common_img, width=141, height=32, bg="#ffffff", borderwidth=2,
                                   relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                   activebackground="#cac669", compound='c',
                                   command=lambda: master.showFrame(charts.Charts)).place(x=291, y=13)

        # chat box displaying the conversation
        self.chatBox = Text(self, bg="#f3f3cc", font=("Helvetica", 10), fg="#005b4b", relief=FLAT, width=59,
                            height=26, wrap=WORD)
        self.chatBox.place(x=9, y=65, width=420, height=450)
        self.chatBox.config(state=DISABLED)

        self.firstChat = False
        # start conversation by a chatbot
        self.beginConversation()

        # make scroll bar
        self.scrollbar = Scrollbar(self, command=self.chatBox.yview)
        self.scrollbar.place(x=422, y=65, height=450)
        self.chatBox['yscrollcommand'] = self.scrollbar.set

        # create entry box
        self.entryBox = Text(self, bg="white", font=("Helvetica", 10), fg="#005b4b", relief=FLAT)
        self.entryBox.place(x=158, y=525, width=280, height=59)

        # submit button
        self.sendButton = Button(self, text="Send", font=("Helvetica", 10), fg="#005b4b", image=self.common_img,
                                 width=141, height=51, bg="#ffffff", borderwidth=2, relief=FLAT,
                                 highlightcolor="#005b4b", highlightbackground="#005b4b", activebackground="#cac669",
                                 compound='c', command=self.sendMessage).place(x=9, y=525)

    def beginConversation(self):
        self.chatBox.config(state=NORMAL)
        self.chatBox.config(foreground="#446665", font=("Helvetica", 10))

        file = open('app.data/data.yaml', 'rb')
        tempFile = open('app.data/tempData.yaml', 'wb')
        decrypt(file, tempFile)

        tempFile.close()
        file.close()

        # read a name from file
        with open('app.data/tempData.yaml', 'r') as tempFile:
            getName = yaml.safe_load(tempFile)
            name = getName['Name']
            # if the name is null, ask for it
            if name is None:
                res = "Hello :) My name is Vivien! I'm here to help you track your Mood. How should I call you?"
                # note that it is the first chat
                self.firstChat = True
            else:
                # start a normal conversation
                res = "Hello " + name + "!"

        tempFile.close()

        with open('app.data/tempData.yaml', 'w'):
            pass

        # insert into the chat box
        self.chatBox.insert(END, "Bot: \n" + res + '\n\n')

        self.chatBox.config(state=DISABLED)
        # show the message at the end of chat box
        self.chatBox.yview(END)

    def sendMessage(self):
        # erase everything from the text widget
        msg = self.entryBox.get("1.0", 'end-1c').strip()
        self.entryBox.delete("0.0", END)

        if msg != '':
            self.chatBox.config(state=NORMAL)
            self.chatBox.insert(END, "You: \n" + msg + '\n\n')
            self.chatBox.config(foreground="#446665", font=("Helvetica", 10))

            # if the chat is the first chat, save the name data into the file
            if self.firstChat is True:
                res = saveNameData(msg)
                # note that the rest of the conversation will not be first chat anymore
                self.firstChat = False
            else:
                # predict class from the written sentence
                ints = predictClass(msg)
                # get response
                res = getResponse(ints, intents)

            self.chatBox.insert(END, "Bot: \n" + res + '\n\n')

            self.chatBox.config(state=DISABLED)
            self.chatBox.yview(END)
