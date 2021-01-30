from datetime import datetime, time
import random

sleepTimes = [21, 7]
matched = {'Meditation': [4, 0, 16, 0], 'Jog': [0], 'Workout': [14, 0, 17, 0, 20, 0, 7, 0]}

def scheduling(matched, sleepTimes):
    for i in matched:
        if matched[i] == 0:
            matched[i] = random.randint(1,24)
    return matched

print(scheduling(matched, sleepTimes))