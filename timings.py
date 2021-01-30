from bs4 import BeautifulSoup

import helpers
import copy

import requests
import re
import nltk
from datetime import datetime, time
import random
import os
import urllib.parse

tasks = input("Enter your tasks for the day (Ex. Meditation, Jog, Workout, Study) : ")

sleep_schedule = input("Enter you Sleep schedule (Ex. 10:00pm to 7:30am) : ")

matched = helpers.my_dictionary()

def convert_activityTimes(act_times):
    tmp_list = []
    for i in range(len(act_times)):
        if not act_times[i] == 'Check':
            tmp_var = list(act_times[i])
            for j in range(len(tmp_var)):
                if tmp_var[j].isnumeric() and tmp_var[j+1].isalpha():
                    tmp_list.append(tmp_var[j] + ':00 ' + tmp_var[j+1].capitalize() + tmp_var[j+2].capitalize())
                if tmp_var[j].isnumeric() and tmp_var[j+1].isnumeric() and tmp_var[j+2].isalpha():
                    tmp_list.append(tmp_var[j] + tmp_var[j+1] + ':00 ' + tmp_var[j+2].capitalize() + tmp_var[j+3].capitalize())

    try:
        tmp_list.remove('0:00 PM')
    except:
        pass

    try:
        tmp_list.remove('0:00 AM')
    except:
        pass

    return tmp_list

def timeToint(list):
    tmp_var = []
    for i in range(len(list)):
        word = list[i]
        var = word.split(':')
        tmp_var.append(var)
    tmp_var = [j for i in tmp_var for j in i]
    return tmp_var


def convertTimes(list):
    sltime_list = []
    for i in range(len(list)):
        sltime_list.append(nltk.word_tokenize(list[i]))

    sltime_list = [j for i in range(len(sltime_list)) for j in sltime_list[i]]

    for i in range(len(sltime_list)):

        if sltime_list[i] == 'PM':
            if sltime_list[i-1] == '1:00':
                sltime_list[i-1] = '13:00'
            if sltime_list[i-1] == '2:00':
                sltime_list[i-1] = '14:00'
            if sltime_list[i-1] == '3:00':
                sltime_list[i-1] = '15:00'
            if sltime_list[i-1] == '4:00':
                sltime_list[i-1] = '16:00'
            if sltime_list[i-1] == '5:00':
                sltime_list[i-1] = '17:00'
            if sltime_list[i-1] == '6:00':
                sltime_list[i-1] = '18:00'
            if sltime_list[i-1] == '7:00':
                sltime_list[i-1] = '19:00'
            if sltime_list[i-1] == '8:00':
                sltime_list[i-1] = '20:00'
            if sltime_list[i-1] == '9:00':
                sltime_list[i-1] = '21:00'
            if sltime_list[i-1] == '10:00':
                sltime_list[i-1] = '22:00'
            if sltime_list[i-1] == '11:00':
                sltime_list[i-1] = '23:00'

    while 'AM' in sltime_list:
        sltime_list.remove('AM')

    while 'PM' in sltime_list:
        sltime_list.remove('PM')

    return sltime_list

def sleep(sleep_schedule):
    tmp_var = []
    tmp_sleep_var = []
    sleep = nltk.word_tokenize(sleep_schedule)

    for i in range(2):
        if sleep[i] == 'to':
            sleep.remove(sleep[i])
        var = list(sleep[i])
        tmp_var.append(var)

    tmp_var = [j for i in tmp_var for j in i]

    for j in range(len(tmp_var)-2):
        if tmp_var[j].isnumeric() and tmp_var[j+1] == ':':
            tmp_sleep_var.append(tmp_var[j]+tmp_var[j+1]+tmp_var[j+2]+tmp_var[j+3] + ' ' + tmp_var[j+4].capitalize() + tmp_var[j+5].capitalize())
        if tmp_var[j].isnumeric() and tmp_var[j+1].isnumeric() and tmp_var[j+2] == ':':
            tmp_sleep_var.append(tmp_var[j]+tmp_var[j+1]+tmp_var[j+2]+tmp_var[j+3]+tmp_var[j+4] + ' ' + tmp_var[j+5].capitalize() + tmp_var[j+6].capitalize())

    sleep = tmp_sleep_var
    try:
        sleep.remove('0:00 PM')
    except:
        pass

    try:
        sleep.remove('0:00 AM')
    except:
        pass

    try:
        sleep.remove('0:30 AM')
    except:
        pass

    try:
        sleep.remove('0:30 PM')
    except:
        pass

    return sleep

def is_time_between(begin_time, end_time, activity_time):
    # If check time is not given, default to current UTC time
    check_time = activity_time
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

def getTime(tasks, sleep_schedule):

    sleepTimes = sleep(sleep_schedule)
    activities = nltk.word_tokenize(tasks)

    for activity in activities:

        if activity != ',':
            url = 'https://www.google.com/search?q=when+is+the+most+ideal+time+to+'+activity+'&rlz=1C1CHBF_enIN932IN932&oq=When+&aqs=chrome.0.69i59l3j69i57j0i67i395i457j69i61l3.2148j1j1&sourceid=chrome&ie=UTF-8'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')

            result = soup.find('div', class_="LGOjhe")
            matched.add(activity,'Check')

            if result is not None:

                sentence = str(result.text).lower()
                words = nltk.word_tokenize(sentence)

                for i in range(len(words)):
                    if words[i] =='am' or words[i] =='pm':
                        matched[activity].append(words[i-1] + words[i])
                    elif words[i] =='morning' or words[i] =='afternoon' or words[i] =='evening' or words[i] =='night' or words[i] == 'sunrise' or words[i] == 'sunset':
                        matched[activity].append(words[i])

    for i in matched:
        for j in range(len(matched[i])):
            if matched[i][j] == "morning":
                matched[i][j] = "7am"
            if matched[i][j] == "afternoon":
                matched[i][j] = "2pm"
            if matched[i][j] == "evening":
                matched[i][j] = "5pm"
            if matched[i][j] == "night":
                matched[i][j] = "8pm"
            if matched[i][j] == "sunrise":
                matched[i][j] = "6am"
            if matched[i][j] == "sunset":
                matched[i][j] = "6pm"

    for each_activity in matched:
        matched[each_activity] = convert_activityTimes(matched[each_activity])


    for i in matched:
        if matched[i] == []:
            matched[i].append("Check")

    for i in matched:
        matched[i] = convertTimes(matched[i])
    sleepTimes = convertTimes(sleepTimes)

    for i in matched:
        matched[i] = timeToint(matched[i])
    sleepTimes = timeToint(sleepTimes)

    for i in matched:
        matched[i] = [int(i) for i in matched[i]]
    sleepTimes = [int(i) for i in sleepTimes]

    tmp_dict = copy.deepcopy(matched)
    print(tmp_dict)

    for i in tmp_dict:
        activity_times = tmp_dict[i]
        for j in range(0, len(activity_times)-1):
            var = activity_times[j]
            var2 = activity_times[j+1]
            if var != 0:
                if var != 30:
                    print(var, var2)
                    if is_time_between( time(sleepTimes[0],sleepTimes[1]), time(sleepTimes[2],sleepTimes[3]), time(var, var2) ) == True:
                        matched[i].remove(var)
                        matched[i].remove(var2)

    for i in matched:
        for j in matched[i]:
            if j == 0 or j == 30:
                matched[i].remove(j)
        if 0 in matched[i]:
            matched[i].remove(0)
        if 30 in matched[i]:
            matched[i].remove(30)

    for i in matched:
        if not matched[i] == []:
            for j in range(0, len(matched[i])+1):
                if matched[i][j] != 0:
                    matched[i].insert(j+1, 0)
            if not (len(matched[i]) % 2) == 0:
                matched[i].append(0)

    return matched, sleepTimes

activity_times, sleepTimes = getTime(tasks, sleep_schedule)

def scheduling(sleepTimes, activity_times):
    pass

for i in activity_times:
    print(f"The most ideal times for {i} are : {activity_times[i]}")
print(sleepTimes)
