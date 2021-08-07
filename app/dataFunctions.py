from datetime import date
import yaml

from dataSupport import count
import dataSecurity as aes

# get today's data
today = date.today()
day = today.strftime("%d.%m")
month = today.strftime("%B")
year = today.strftime("Year_%Y")

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
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "February": {
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "March": {
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "April": {
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "May": {
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "June": {
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "July": {
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "August": {
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "September": {
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "October": {
                 "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "November": {
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
            "December": {
                "Dates": [{
                    "Date": None,
                    "Mood_name": None,
                    "Mood": None}]},
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


# get data from file to plot
def getData(chart, data):
    file = open('app.data/data.yaml', 'rb')
    tempFile = open('app.data/tempData.yaml', 'wb')
    aes.decrypt(file, tempFile)

    tempFile.close()
    file.close()

    with open('app.data/tempData.yaml', 'r') as tempFile:
        # load the file
        d = yaml.safe_load(tempFile)
        # get the number of years in file
        c = len(d[chart]['Years'])
        # get data from the current month
        dataToPlot = d[chart]['Years'][c - 1][year][month][data]

        # data for 1st chart
        if data == "Dates":
            numberOfDates = count(d[chart]['Years'][c - 1][year][month], "Date")

            # check if the number of elements is smaller than 31
            if numberOfDates < 31:
                # if it is, get data from previous month
                # get number of the current month by a switcher and subtract 1 to get previous month
                previousMonth = switchMonthNumber.get(month) - 1
                # come back to month name format
                previousMonth = switchNumberMonth.get(previousMonth)
                # get data from the previous month
                previous_month_data = d[chart]['Years'][c - 1][year][previousMonth][data]

                with open('app.data/tempData.yaml', 'w'):
                    pass

                return dataToPlot, previous_month_data, numberOfDates

        # data for 2nd chart
        if data == "Moods":
            # get data from the previous month
            previousMonth1 = switchMonthNumber.get(month) - 1
            previousMonth1 = switchNumberMonth.get(previousMonth1)
            previousMonthData = d[chart]['Years'][c - 1][year][previousMonth1][data]

            # get data from the third month
            previousMonth2 = switchMonthNumber.get(previousMonth1) - 1
            previousMonth2 = switchNumberMonth.get(previousMonth2)
            previousMonthData2 = d[chart]['Years'][c - 1][year][previousMonth2][data]

            # list of months will become the x ticks
            months = [previousMonth2, previousMonth1, month]

            with open('app.data/tempData.yaml', 'w'):
                pass

            return dataToPlot, previousMonthData, previousMonthData2, months


def checkIfYearExists():
    file = open('app.data/data.yaml', 'rb')
    tempFile = open('app.data/tempData.yaml', 'wb')
    aes.decrypt(file, tempFile)

    tempFile.close()
    file.close()

    with open('app.data/tempData.yaml', 'r') as tempFile:
        d = yaml.safe_load(tempFile)
        # look for a current year in a file
        num = count(d['Date_chart']['Years'], year)

        # if it doesn't exist make space for new data
        if num == 0:
            # append those data to the file
            d['Date_chart']['Years'].append(addDates)
            d['Mood_chart']['Years'].append(addMoods)
    if d:
        # write into the file
        with open('app.data/tempData.yaml', 'w') as tempFile:
            yaml.safe_dump(d, tempFile, sort_keys=False)

        tempFile.close()

    tempFile = open('app.data/tempData.yaml', 'rb')
    file = open('app.data/data.yaml', 'wb')
    aes.encrypt(tempFile, file)

    tempFile.close()
    file.close()

    with open('app.data/tempData.yaml', 'w'):
        pass


def checkIfDateExists():
    # check if year exists and add new data if it doesn't
    checkIfYearExists()

    file = open('app.data/data.yaml', 'rb')
    tempFile = open('app.data/tempData.yaml', 'wb')
    aes.decrypt(file, tempFile)

    tempFile.close()
    file.close()

    with open('app.data/tempData.yaml', 'r') as tempFile:
        d = yaml.safe_load(tempFile)
        # get number of years from the date chart data
        c = len(d['Date_chart']['Years'])
        # count number of dates in the current month
        num = count(d['Date_chart']['Years'][c - 1][year][month], "Date")

        exist = False

        for i in range(num):
            # checking if data for that day was already recorded
            if d['Date_chart']['Years'][c - 1][year][month]['Dates'][i]['Date'] == day:
                exist = True

    tempFile.close()

    with open('app.data/tempData.yaml', 'w'):
        pass

    return exist


def saveNameData(name):
    file = open('app.data/data.yaml', 'rb')
    tempFile = open('app.data/tempData.yaml', 'wb')
    aes.decrypt(file, tempFile)

    tempFile.close()
    file.close()

    # load the file
    with open('app.data/tempData.yaml', 'r') as tempFile:
        writeName = yaml.safe_load(tempFile)

    if writeName:
        with open('app.data/tempData.yaml', 'w') as tempFile:
            # set the name and write into the file
            writeName['Name'] = name
            yaml.safe_dump(writeName, tempFile, sort_keys=False)

        # return the response to continue the chat
        return "Hello " + name + "! Your name has been saved :) How are you feeling today?"

    tempFile.close()

    tempFile = open('app.data/tempData.yaml', 'rb')
    file = open('app.data/data.yaml', 'wb')
    aes.encrypt(tempFile, file)

    tempFile.close()
    file.close()

    with open('app.data/tempData.yaml', 'w'):
        pass


def saveMoodData(data):
    # data to append
    newData = {
        'Date': day,
        'Mood_name': data,
        'Mood': switchMoodNumber.get(data)
    }

    file = open('app.data/data.yaml', 'rb')
    tempFile = open('app.data/tempData.yaml', 'wb')
    aes.decrypt(file, tempFile)

    tempFile.close()
    file.close()

    with open('app.data/tempData.yaml', 'r') as tempFile:
        addData = yaml.safe_load(tempFile)
        c = len(addData['Date_chart']['Years'])
        # save data for the first chart
        addData['Date_chart']['Years'][c - 1][year][month]['Dates'].append(newData)
        # update number of occurrences of that mood
        addData['Mood_chart']['Years'][c - 1][year][month]['Moods'][0][data] += 1

    if addData:
        # write data into the file
        with open('app.data/tempData.yaml', 'w') as temFile:
            yaml.safe_dump(addData, tempFile, sort_keys=False)

        tempFile.close()

    tempFile = open('app.data/tempData.yaml', 'rb')
    file = open('app.data/data.yaml', 'wb')
    aes.encrypt(tempFile, file)

    tempFile.close()
    file.close()

    with open('app.data/tempData.yaml', 'w'):
        pass
