"""
Marta Dzięgielewska
Projekt dyplomowy inżynierski: Przykłady wykorzystania sztucznej inteligencji w psychologii
Promotor: dr inż Paweł Syty
"""

from tkinter import *

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from dataFunctions import *

import appChat as chat
import appSettings as settings


# FRAME CLASS WITH CHARTS
class Charts(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(width=450, height=600, bg="#f3f3cc")
        # to have a better control of the size of elements
        self.common_img = PhotoImage(width=1, height=1)

        # menu
        self.settingsButton = Button(self, text="Settings", font=("Helvetica", 10), fg="#005b4b",
                                     image=self.common_img, width=141, height=32, bg="#ffffff", borderwidth=2,
                                     relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                     activebackground="#cac669", compound='c',
                                     command=lambda: master.showFrame(settings.Settings)).place(x=9, y=13)

        self.chatButton = Button(self, text="Chat", font=("Helvetica", 10), fg="#005b4b", image=self.common_img,
                                 width=141, height=32, bg="#ffffff", borderwidth=2, relief=FLAT,
                                 highlightcolor="#005b4b", highlightbackground="#005b4b", activebackground="#cac669",
                                 compound='c', command=lambda: master.showFrame(chat.Chat)).place(x=150, y=13)

        self.graphsButton = Button(self, text="Charts", font=("Helvetica", 10), fg="#005b4b",
                                   image=self.common_img, width=141, height=32, bg="#cac669", borderwidth=2,
                                   relief=FLAT, highlightcolor="#005b4b", highlightbackground="#005b4b",
                                   activebackground="#cac669", compound='c').place(x=291, y=13)

        # 1ST CHART
        self.canvasDateChart = Canvas(self, height=225, width=400)
        self.canvasDateChart.place(x=45, y=90)

        # chart 225x400 px
        self.dateFigure = Figure(figsize=(3.7, 2.1), dpi=96, tight_layout=True)
        self.dateAxes = self.dateFigure.add_subplot(111)

        # line chart
        self.line = FigureCanvasTkAgg(self.dateFigure, self.canvasDateChart)
        self.line.get_tk_widget().pack()

        # set title and hide axis labels
        self.dateAxes.set_title("Your mood for the last 31 days", fontsize=8)
        self.dateAxes.xaxis.label.set_visible(False)

        # get data for the first chart
        self.monthDataToPlot, self.xLabels = getData('Date_chart', 'Dates')

        # plot data
        self.monthDataToPlot.plot(kind='line', legend=False, ax=self.dateAxes, color='#10451D', marker='.',  fontsize=7)

        # scale the x axis
        # set frequency of x ticks
        self.xTicks = np.arange(0, 31, 6)
        self.dateAxes.set_xticks(self.xTicks, minor=False)

        self.xMinorTicks = np.arange(0, 31, 1)
        self.dateAxes.set_xticks(self.xMinorTicks, minor=True)

        self.xLabels = [self.xLabels[6 * i] for i in range(6)]
        self.dateAxes.set_xticklabels(self.xLabels, fontdict=None, minor=False, fontsize=7)

        # scale the y axis
        # set frequency of y ticks
        self.yTicks = np.arange(0, 10, 1)
        self.dateAxes.set_yticks(self.yTicks, minor=False)

        self.yLabels = ["Depressed", "Anxious", "Stressed", "Sad", "Angry", "Tired", "Neutral", "Okay", "Happy",
                        "Very happy"]
        self.dateAxes.set_yticklabels(self.yLabels, fontdict=None, minor=False, fontsize=7)

        # set y grid
        self.dateAxes.yaxis.grid(True, linestyle='dashed', alpha=0.25)

        # 2ND CHART
        self.canvasMoodChart = Canvas(self, height=250, width=400)
        self.canvasMoodChart.place(x=45, y=315)

        # chart 350x250 px
        self.moodFigure = Figure(figsize=(3.7, 2.6), dpi=96)
        self.moodAxes = self.moodFigure.add_subplot(111)

        # bar chart
        self.bar = FigureCanvasTkAgg(self.moodFigure, self.canvasMoodChart)
        self.bar.get_tk_widget().pack()

        # set title and hide axis labels
        self.moodAxes.set_title("Your mood for the last 3 months", fontsize=8)
        self.moodAxes.xaxis.label.set_visible(False)

        # get data for the second chart
        self.moodData, self.previousMood, self.previousMood2, self.xTicks = getData('Mood_chart', 'Moods')

        # current month
        self.df2 = DataFrame(self.previousMood2)
        # change row with column
        self.df2 = self.df2.T
        # name the column after the current month
        self.df2.columns = [self.xTicks[0]]

        # previous two months
        self.df21 = DataFrame(self.previousMood)
        self.df21 = self.df21.T
        self.df21.columns = [self.xTicks[1]]

        self.df22 = DataFrame(self.moodData)
        self.df22 = self.df22.T
        self.df22.columns = [self.xTicks[2]]

        # combine three dataframes
        self.df2 = concat([self.df2, self.df21, self.df22], axis=1)
        self.df2 = self.df2.T

        # plot data
        self.df2.plot(kind='bar', legend=False, width=1, ax=self.moodAxes, fontsize=7,
                      color={'veryhappy': '#b7efc5', 'happy': '#92e6a7', 'ok': '#6ede8a', 'neutral': '#4ad66d',
                             'tired': '#2dc653', 'angry': '#25a244', 'sad': '#208b3a', 'stressed': '#1a7431',
                             'anxious': '#155d27', 'depressed': '#10451d'})

        # set the legend
        self.moodAxes.legend(['Very Happy', 'Happy', 'Ok', 'Neutral', 'Tired', 'Angry', 'Sad', 'Stressed', 'Anxious',
                              'Depressed'], fontsize=7, loc='upper center', ncol=3)

        # scale y axis
        # set x ticks labels
        self.moodAxes.set_xticklabels(self.xTicks, rotation=0)
        # set frequency of y ticks
        self.yTicks = np.arange(0, 25, 2)
        self.moodAxes.set_yticks(self.yTicks)

        # set y grid and its params
        self.moodAxes.yaxis.grid(True, linestyle='dashed', alpha=0.25, zorder=0)
        self.moodAxes.set_axisbelow(True)
