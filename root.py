from tkinter import *
import chatbot


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Mood Tracker")
        self.geometry("450x600")
        self.iconbitmap('logo.ico')
        self.resizable(width=FALSE, height=FALSE)
        self.configure(background="#f3f3cc")
        self.current_frame = None

        self.show_frame(chatbot.Chat)

    def show_frame(self, page_name):
        new_frame = page_name(self)
        if self.current_frame is not None:
            self.current_frame.pack_forget()

        self.current_frame = new_frame
        self.current_frame.pack()


if __name__ == "__main__":
    app = App()
    mainloop()
