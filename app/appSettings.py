from tkinter import *
from PIL import ImageTk, Image
import yaml

from dataSecurity import *

import appChat as chat
import appCharts as charts


# FRAME CLASS WITH SETTINGS
class Settings(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(width=450, height=600, bg="#f3f3cc")
        # to have a better control of the size of elements
        self.common_img = PhotoImage(width=1, height=1)

        # menu
        self.settingsButton = Button(self, text="Settings", font=("Helvetica", 10), fg="#005b4b",
                                     image=self.common_img, width=141, height=32, bg="#cac669", borderwidth=2,
                                     relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                     activebackground="#cac669", compound='c').place(x=9, y=13)

        self.chatButton = Button(self, text="Chat", font=("Helvetica", 10), fg="#005b4b", image=self.common_img,
                                 width=141, height=32, bg="#ffffff", borderwidth=2, relief=FLAT,
                                 highlightcolor="#005b4b", highlightbackground="#005b4b", activebackground="#cac669",
                                 compound='c', command=lambda: master.showFrame(chat.Chat)).place(x=150, y=13)

        self.chartButton = Button(self, text="Charts", font=("Helvetica", 10), fg="#005b4b",
                                  image=self.common_img, width=141, height=32, bg="#ffffff", borderwidth=2,
                                  relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                  activebackground="#cac669", compound='c',
                                  command=lambda: master.showFrame(charts.Charts)).place(x=291, y=13)

        # edit name
        self.nameLabel = Label(self, text="Change your name:", justify=LEFT, bg="#f3f3cc", font=("Helvetica", 10),
                               fg="#005b4b", relief=FLAT)
        self.nameLabel.place(x=30, y=81, width=250, height=32)

        self.name = Text(self, bg="white", font=("Helvetica", 10), fg="#005b4b", relief=FLAT)
        self.name.place(x=96, y=117, width=250, height=30)

        self.submitButton = Button(self, text="Submit", font=("Helvetica", 10), fg="#005b4b", image=self.common_img,
                                   width=50, height=15, bg="#ffffff", borderwidth=2, relief=FLAT,
                                   highlightcolor="#005b4b", highlightbackground="#005b4b", activebackground="#cac669",
                                   compound='c', command=self.changeName).place(x=287, y=160)

        self.changesSaved = Label(self, text="Changes have been saved", justify=LEFT, bg="#f3f3cc",
                                  font=("Helvetica", 10), fg="#005b4b", relief=FLAT)

        # introduction + logo
        self.introduction = Label(self, text="Hello! I'm Chat bot Vivien :)", bg="#f3f3cc",
                                  font=("Helvetica", 10), fg="#005b4b", relief=FLAT)
        self.introduction.place(x=100, y=215, width=250, height=32)

        self.canvas = Canvas(self, height=150, width=150, bg="#f3f3cc")
        self.canvas.place(x=145, y=255)

        self.logo = ImageTk.PhotoImage(Image.open("app.images/logo.png"))
        self.canvas.create_image(77, 77, image=self.logo)

        # contact info
        self.contact = Label(self, text="Contact me:", justify=LEFT, bg="#f3f3cc", font=("Helvetica", 10),
                             fg="#005b4b", relief=FLAT)
        self.contact.place(x=10, y=450, width=250, height=32)

        self.author = Label(self, text="Marta Dzięgielewska", justify=LEFT, bg="#f3f3cc", font=("Helvetica", 10),
                            fg="#005b4b", relief=FLAT)
        self.author.place(x=77, y=490, width=250, height=32)

        self.author = Label(self, text="marta.dziegielewska99@gmail.com", justify=LEFT, bg="#f3f3cc",
                            font=("Helvetica", 10), fg="#005b4b", relief=FLAT)
        self.author.place(x=120, y=520, width=250, height=32)

    def changeName(self):
        # erase everything from the text widget
        newName = self.name.get("1.0", 'end-1c').strip()
        self.name.delete("0.0", END)

        if newName != '':
            self.name.config(state=NORMAL)

            file = open('app.data/data.yaml', 'rb')
            tempFile = open('app.data/tempData.yaml', 'wb')
            decrypt(file, tempFile)

            tempFile.close()
            file.close()

            # load a file to save data
            with open('app.data/tempData.yaml', 'r') as tempFile:
                data = yaml.safe_load(tempFile)
                data['Name'] = newName

            if data:
                # write into the file
                with open('app.data/tempData.yaml', 'w') as tempFile:
                    yaml.safe_dump(data, tempFile, sort_keys=False)

                    # print the info
                    self.changesSaved.place(x=96, y=160)

            tempFile.close()

            tempFile = open('app.data/tempData.yaml', 'rb')
            file = open('app.data/data.yaml', 'wb')
            encrypt(tempFile, file)

            tempFile.close()
            file.close()

            with open('app.data/tempData.yaml', 'w'):
                pass
