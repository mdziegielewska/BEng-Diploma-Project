from tkinter import *
from PIL import ImageTk, Image

import chatbot
import charts


class Settings(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(width=450, height=600, bg="#f3f3cc")

        self.common_img = PhotoImage(width=1, height=1)

        # menu
        self.settings_button = Button(self, text="Settings", font=("Helvetica", 10), fg="#005b4b",
                                      image=self.common_img, width=141, height=32, bg="#cac669", borderwidth=2,
                                      relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                      activebackground="#cac669", compound='c',
                                      command=lambda: master.show_frame(Settings)).place(x=9, y=13)

        self.chat_button = Button(self, text="Chat", font=("Helvetica", 10), fg="#005b4b", image=self.common_img,
                                  width=141, height=32, bg="#ffffff", borderwidth=2, relief=FLAT,
                                  highlightcolor="#005b4b", highlightbackground="#005b4b", activebackground="#cac669",
                                  compound='c', command=lambda: master.show_frame(chatbot.Chat)).place(x=150, y=13)

        self.charts_button = Button(self, text="Charts", font=("Helvetica", 10), fg="#005b4b",
                                    image=self.common_img, width=141, height=32, bg="#ffffff", borderwidth=2,
                                    relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                    activebackground="#cac669", compound='c',
                                    command=lambda: master.show_frame(charts.Charts)).place(x=291, y=13)

        # editing name
        self.name_label = Label(self, text="Change your name:", justify=LEFT, bg="#f3f3cc", font=("Helvetica", 10),
                                fg="#005b4b", relief=FLAT)
        self.name_label.place(x=30, y=81, width=250, height=32)

        self.name = Text(self, bg="white", font=("Helvetica", 10), fg="#005b4b", relief=FLAT)
        self.name.place(x=96, y=117, width=250, height=30)

        self.submit_button = Button(self, text="Submit", font=("Helvetica", 10), fg="#005b4b", image=self.common_img,
                                    width=50, height=15, bg="#ffffff", borderwidth=2, relief=FLAT,
                                    highlightcolor="#005b4b", highlightbackground="#005b4b", activebackground="#cac669",
                                    compound='c').place(x=287, y=160)

        # introduction + logo
        self.introduction = Label(self, text="Hello! I'm Chat bot Vivien :)", bg="#f3f3cc",
                                  font=("Helvetica", 10), fg="#005b4b", relief=FLAT)
        self.introduction.place(x=100, y=215, width=250, height=32)

        self.canvas = Canvas(self, height=150, width=150, bg="#f3f3cc")
        self.canvas.place(x=145, y=255)

        self.logo = ImageTk.PhotoImage(Image.open("logo.png"))
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
