"""
Marta Dzięgielewska
Projekt dyplomowy inżynierski: Przykłady wykorzystania sztucznej inteligencji w psychologii
Promotor: dr inż Paweł Syty
"""

from datetime import date

# get today's data
today = date.today()

todaysDate = today.strftime("%d")
day = today.strftime("%d.%m")

month = today.strftime("%B")

year = today.strftime("Year_%Y")
previousYear = "Year_" + str(int(today.strftime("%Y")) - 1)


# count elements in a file
def count(d, s):
    c = 0
    if isinstance(d, dict):
        for k, v in d.items():
            if k == s:
                c += 1
            c += count(v, s)
    elif isinstance(d, list):
        for l in d:
            c += count(l, s)
    return c


# month to number switcher
switchMonthNumber = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

# number to month switcher
switchNumberMonth = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# mood name to number switcher
switchMoodNumber = {
    "veryhappy": 9,
    "happy": 8,
    "ok": 7,
    "neutral": 6,
    "tired": 5,
    "angry": 4,
    "sad": 3,
    "stressed": 2,
    "anxious": 1,
    "depressed": 0
}

# 1st data
addDates = {year: {
    "January": {
        "Dates": [
            {
                "Date": "01.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.01",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "31.01",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "February": {
        "Dates": [
            {
                "Date": "01.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.02",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.02",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "March": {
        "Dates": [
            {
                "Date": "01.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.03",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.03",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "April": {
        "Dates": [
            {
                "Date": "01.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.04",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "31.04",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "May": {
        "Dates": [
            {
                "Date": "01.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.05",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "31.05",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "June": {
        "Dates": [
            {
                "Date": "01.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.06",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.06",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "July": {
        "Dates": [
            {
                "Date": "01.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.07",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "31.07",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "August": {
        "Dates": [
            {
                "Date": "01.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.08",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "31.08",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "September": {
        "Dates": [
            {
                "Date": "01.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.09",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.09",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "October": {
        "Dates": [
            {
                "Date": "01.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.10",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "31.10",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "November": {
        "Dates": [
            {
                "Date": "01.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.11",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.11",
                "Mood_name": None,
                "Mood": None
            }
        ]},
    "December": {
        "Dates": [
            {
                "Date": "01.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "02.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "03.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "04.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "05.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "06.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "07.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "08.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "09.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "10.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "11.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "12.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "13.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "14.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "15.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "16.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "17.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "18.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "19.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "20.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "21.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "22.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "23.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "24.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "25.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "26.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "27.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "28.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "29.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "30.12",
                "Mood_name": None,
                "Mood": None
            },
            {
                "Date": "31.12",
                "Mood_name": None,
                "Mood": None
            }
        ]},
}}

# 2nd data
addMoods = {year: {
    "January": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "February": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "March": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "April": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "May": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "June": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "July": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "August": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "September": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "October": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "November": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]},
    "December": {
        "Moods": [{
            "veryhappy": 0,
            "happy": 0,
            "ok": 0,
            "neutral": 0,
            "tired": 0,
            "angry": 0,
            "sad": 0,
            "stressed": 0,
            "anxious": 0,
            "depressed": 0}]}
}}
