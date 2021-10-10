from tkinter import *

import appChat as chat


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Mood Tracker")
        self.geometry("450x600")
        self.iconbitmap('appImages/logoIcon.ico')
        self.resizable(width=FALSE, height=FALSE)
        self.configure(background="#f3f3cc")
        self.currentFrame = None

        self.showFrame(chat.Chat)

    def showFrame(self, pageName):
        newFrame = pageName(self)
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()

        self.currentFrame = newFrame
        self.currentFrame.pack()


if __name__ == "__main__":
    app = App()
    mainloop()
