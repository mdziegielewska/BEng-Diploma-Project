import yaml
from pandas import DataFrame, concat

from dataSupport import *
import dataSecurity as aes


# get data from file to plot
def getData(chart, data):
    file = open('appData/data.yaml', 'rb')
    tempFile = open('appData/tempData.yaml', 'wb')
    aes.decrypt(file, tempFile)

    tempFile.close()
    file.close()

    with open('appData/tempData.yaml', 'r') as tempFile:
        # load the file
        d = yaml.safe_load(tempFile)
        # get the number of years in file
        c = len(d[chart]['Years'])
        # get data from the current month
        dataToPlot = d[chart]['Years'][c - 1][year][month][data]

        # data for 1st chart
        if data == "Dates":
            dataToPlot = DataFrame(dataToPlot, columns=['Date', 'Mood'])
            # first element in each Date is null
            dataToPlot = dataToPlot.loc[:int(todaysDate)-1]

            numberOfDates = dataToPlot['Date'].count()

            # check if the number of elements is smaller than 31
            if numberOfDates < 31:
                if month == "January":
                    # need to get data from the previous year
                    previousMonthData = d[chart]['Years'][c - 2][previousYear]['December'][data]
                else:
                    # if it is, get data from previous month
                    # get number of the current month by a switcher and subtract 1 to get previous month
                    previousMonth = switchMonthNumber.get(month) - 1
                    # come back to month name format
                    previousMonth = switchNumberMonth.get(previousMonth)
                    # get data from the previous month
                    previousMonthData = d[chart]['Years'][c - 1][year][previousMonth][data]

                additionalData = DataFrame(previousMonthData, columns=['Date', 'Mood'])

            if additionalData is not None:
                # number of elements says how much data do we need
                previousData = additionalData.loc[int(todaysDate)-1:]

                # combine two dataframes
                dataToPlot = concat([previousData, dataToPlot], ignore_index=True, names='Dates')
                xLabels = dataToPlot['Date']
                # set list of dates as our dependent variable
                dataToPlot = dataToPlot[['Date', 'Mood']].groupby('Date', sort=False).sum(min_count=1)

            with open('appData/tempData.yaml', 'w'):
                pass

            return dataToPlot, xLabels

        # data for 2nd chart
        if data == "Moods":
            if month == "January":
                previousMonth1 = "December"
                previousMonth2 = "November"

                # need to get data from the last two months of the previous year
                previousMonthData = d[chart]['Years'][c - 2][previousYear][previousMonth1][data]
                previousMonthData2 = d[chart]['Years'][c - 2][previousYear][previousMonth2][data]

            elif month == "February":
                previousMonth1 = switchNumberMonth.get(switchMonthNumber.get(month) - 1)
                previousMonth2 = "December"

                # need to get data from January and previous year December
                previousMonthData = d[chart]['Years'][c - 1][year][previousMonth1][data]
                previousMonthData2 = d[chart]['Years'][c - 2][previousYear][previousMonth2][data]

            else:
                # get data from the previous month
                previousMonth1 = switchNumberMonth.get(switchMonthNumber.get(month) - 1)
                # get data from the third month
                previousMonth2 = switchNumberMonth.get(switchMonthNumber.get(previousMonth1) - 1)

                previousMonthData = d[chart]['Years'][c - 1][year][previousMonth1][data]
                previousMonthData2 = d[chart]['Years'][c - 1][year][previousMonth2][data]

            # list of months will become the x ticks
            months = [previousMonth2, previousMonth1, month]

            with open('appData/tempData.yaml', 'w'):
                pass

            return dataToPlot, previousMonthData, previousMonthData2, months


def checkIfYearExists():
    file = open('appData/data.yaml', 'rb')
    tempFile = open('appData/tempData.yaml', 'wb')
    aes.decrypt(file, tempFile)

    tempFile.close()
    file.close()

    with open('appData/tempData.yaml', 'r') as tempFile:
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
        with open('appData/tempData.yaml', 'w') as tempFile:
            yaml.safe_dump(d, tempFile, sort_keys=False)

        tempFile.close()

    tempFile = open('appData/tempData.yaml', 'rb')
    file = open('appData/data.yaml', 'wb')
    aes.encrypt(tempFile, file)

    tempFile.close()
    file.close()

    with open('appData/tempData.yaml', 'w'):
        pass


def checkIfDateExists():
    # check if year exists and add new data if it doesn't
    checkIfYearExists()

    file = open('appData/data.yaml', 'rb')
    tempFile = open('appData/tempData.yaml', 'wb')
    aes.decrypt(file, tempFile)

    tempFile.close()
    file.close()

    with open('appData/tempData.yaml', 'r') as tempFile:
        d = yaml.safe_load(tempFile)
        # get number of years from the date chart data
        c = len(d['Date_chart']['Years'])
        # count number of dates in the current month
        num = count(d['Date_chart']['Years'][c - 1][year][month], "Date")

        exist = False

        for i in range(num):
            # checking if data for that day was already recorded
            if d['Date_chart']['Years'][c - 1][year][month]['Dates'][i]['Date'] == day:
                if d['Date_chart']['Years'][c - 1][year][month]['Dates'][i]['Mood'] is not None:
                    if d['Date_chart']['Years'][c - 1][year][month]['Dates'][i]['Mood_name'] is not None:
                        exist = True

    tempFile.close()

    with open('appData/tempData.yaml', 'w'):
        pass

    return exist


def saveNameData(name):
    file = open('appData/data.yaml', 'rb')
    tempFile = open('appData/tempData.yaml', 'wb')
    aes.decrypt(file, tempFile)

    tempFile.close()
    file.close()

    # load the file
    with open('appData/tempData.yaml', 'r') as tempFile:
        writeName = yaml.safe_load(tempFile)

    if writeName:
        # set the name
        writeName['Name'] = name

        with open('appData/tempData.yaml', 'w') as tempFile:
            # write into the file
            yaml.safe_dump(writeName, tempFile, sort_keys=False)

        tempFile.close()

    tempFile = open('appData/tempData.yaml', 'rb')
    file = open('appData/data.yaml', 'wb')
    aes.encrypt(tempFile, file)

    tempFile.close()
    file.close()

    with open('appData/tempData.yaml', 'w'):
        pass

    # return the response to continue the chat
    return "Hello " + name + "! Your name has been saved :) How are you feeling today? \nMy system is able to " \
                             "recognize 10 moods: really happy, happy, ok, neutral, tired, angry, sad, stressed, " \
                             "anxious or depressed. But you can try to "


def saveMoodData(data):
    file = open('appData/data.yaml', 'rb')
    tempFile = open('appData/tempData.yaml', 'wb')
    aes.decrypt(file, tempFile)

    tempFile.close()
    file.close()

    with open('appData/tempData.yaml', 'r') as tempFile:
        addData = yaml.safe_load(tempFile)
        c = len(addData['Date_chart']['Years'])

    if addData:
        # save data for the first chart
        addData['Date_chart']['Years'][c - 1][year][month]['Dates'][int(todaysDate)-1]['Mood_name'] = data
        addData['Date_chart']['Years'][c - 1][year][month]['Dates'][int(todaysDate)-1]['Mood'] = switchMoodNumber.get(
            data)
        # update number of occurrences of that mood
        addData['Mood_chart']['Years'][c - 1][year][month]['Moods'][0][data] += 1

        # write data into the file
        with open('appData/tempData.yaml', 'w') as tempFile:
            yaml.safe_dump(addData, tempFile, sort_keys=False)

        tempFile.close()

    tempFile = open('appData/tempData.yaml', 'rb')
    file = open('appData/data.yaml', 'wb')
    aes.encrypt(tempFile, file)

    tempFile.close()
    file.close()

    with open('appData/tempData.yaml', 'w'):
        pass


def countLowDays():
    # get mood data from the last 31 days
    monthData, dates = getData('Date_chart', 'Dates')

    # count days with lowered mood
    lowDaysNumber = sum(map(lambda x: x < 4, monthData['Mood'].tolist()))

    return lowDaysNumber
