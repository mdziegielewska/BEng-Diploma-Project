from tkinter import *
import settings
import charts


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
