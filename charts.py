from tkinter import *
from pandas import DataFrame, pivot_table
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import chatbot
import settings


class Charts(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(width=450, height=600, bg="#f3f3cc")

        self.common_img = PhotoImage(width=1, height=1)

        # menu
        self.settings_button = Button(self, text="Settings", font=("Helvetica", 10), fg="#005b4b",
                                      image=self.common_img, width=141, height=32, bg="#ffffff", borderwidth=2,
                                      relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                      activebackground="#cac669", compound='c',
                                      command=lambda: master.show_frame(settings.Settings)).place(x=9, y=13)

        self.chat_button = Button(self, text="Chat", font=("Helvetica", 10), fg="#005b4b", image=self.common_img,
                                  width=141, height=32, bg="#ffffff", borderwidth=2, relief=FLAT,
                                  highlightcolor="#005b4b", highlightbackground="#005b4b", activebackground="#cac669",
                                  compound='c', command=lambda: master.show_frame(chatbot.Chat)).place(x=150, y=13)

        self.graphs_button = Button(self, text="Charts", font=("Helvetica", 10), fg="#005b4b",
                                    image=self.common_img, width=141, height=32, bg="#cac669", borderwidth=2,
                                    relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                    activebackground="#cac669", compound='c',
                                    command=lambda: master.show_frame(Charts)).place(x=291, y=13)

        # 1st chart
        self.canvas_chart1 = Canvas(self, height=200, width=250)
        self.canvas_chart1.place(x=155, y=90)

        self.legend = Label(self, text="9 - very happy\n8 - happy\n7 - okay\n6 - neutral\n5 - tired\n4 - angry\n"
                                       "3 - sad\n2 - stressed\n1 - anxious\n0 - depressed", justify=LEFT, bg="#f3f3cc",
                            font=("Helvetica", 10), fg="#005b4b", relief=FLAT)
        self.legend.place(x=20, y=85, width=110, height=200)

        self.data1 = {'Date': ['01.05', '02.05', '03.05', '04.05', '05.05', '06.05'],
                      'Mood_name': ['Happy', 'Anxious', 'Anxious', 'Tired', 'Anxious', 'Angry'],
                      'Mood': [8, 1, 1, 5, 1, 4]}
        self.df1 = DataFrame(self.data1, columns=['Date', 'Mood_name', 'Mood'])

        self.figure1 = Figure(figsize=(2.6, 2), dpi=96, tight_layout=True)
        self.axes1 = self.figure1.add_subplot(111)

        self.line = FigureCanvasTkAgg(self.figure1, self.canvas_chart1)
        self.line.get_tk_widget().pack()

        self.df1 = self.df1[['Date', 'Mood']].groupby('Date').sum()
        self.df1.plot(kind='line', legend=False, ax=self.axes1, color='#004529', marker='.', fontsize=7)
        self.axes1.set_title("Your mood for the last 30 days", fontsize=8)
        self.axes1.xaxis.label.set_visible(False)

        # 2nd chart
        self.canvas_chart2 = Canvas(self, height=250, width=300)
        self.canvas_chart2.place(x=78, y=315)

        self.x_ticks = ['March', 'April', 'May']
        self.data2 = {'Month': [3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],
                      'Mood': [1, 4, 5, 8, 1, 4, 5, 8, 1, 4, 5, 8],
                      'Number': [6, 8, 15, 2, 10, 8, 11, 1, 7, 10, 11, 3]}
        self.df2 = DataFrame(self.data2, columns=['Month', 'Mood', 'Number'])

        # preparing data to plot
        self.df_pivot = pivot_table(self.df2, values='Number', index='Month', columns='Mood', aggfunc=np.mean)

        self.figure2 = Figure(figsize=(3.125, 2.6), dpi=96)
        self.axes2 = self.figure2.add_subplot(111)

        self.line2 = FigureCanvasTkAgg(self.figure2, self.canvas_chart2)
        self.line2.get_tk_widget().pack()

        self.df_pivot.plot(kind='bar', legend=False, ax=self.axes2, fontsize=7,
                           color={1: '#004529', 4: '#006837', 5: '#238443', 8: '#41ab5d'})

        self.axes2.set_title("Your mood for the last 3 months", fontsize=8)
        self.axes2.set_xticklabels(self.x_ticks, rotation=0)
        self.axes2.legend(['Anxious', 'Angry', 'Tired', 'Happy'], fontsize=7)
        self.axes2.xaxis.label.set_visible(False)
