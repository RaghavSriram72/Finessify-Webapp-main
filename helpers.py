

from flask import redirect, render_template, request, session
from functools import wraps


class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = []
        self[key].append(value)

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def speechRecognizer():

    speech_recognized = []

#    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say the activity you want to input and its priority(High/Low) Ex.Workout under High Priority")
        audio = recognizer.listen(source)

    speech = recognizer.recognize_google(audio)
    tokens = nltk.word_tokenize(speech.lower())

    high = True
    for value in tokens:
        if value == low:
            high = False

    def priority(high):
        return 'High' if high == True else 'Low'

    result_priority = priority(high)
    Activity = tokens[0]
    Priority = result_priority
    Speech = speech

    speech_recognized.append(Activity)
    speech_recognized.append(Priority)
    speech_recognized.append(speech)

    return speech_recognized

# act = []

# for activity in activities:
#     if activity in Timings:
#         act.append(activity)

# print(act)

# def getTime2(Timings, sleep, act):

#     times = []
#     for i in range(len(Timings)):
#         for each_character in Timings[i]:
#             if each_character.isdigit():
#                 times.append(Timings[i])



# for i in range(len(Timings)):
#     if Timings[i] == act[0] or Timings[i] == act[1] or Timings[i] == act[2] or Timings[i] == act[3]:
#         if not Timings[i+1] == None or Timings[i+1] == act[0] or Timings[i+1] == act[1] or Timings[i+1] == act[2] or Timings[i+1] == act[3] or Timings[i+1] == act[4]:
#             act.remove(Timings[i])
#             new_time = getTime2(Timings, sleep, act)

def getArticle():
    user_streak = True

    # to search
    query = ["Guides on Time Management", "Guides on Mental Health"]

    if user_streak == True:
        for i in range(len(query)):
            for j in search(query[i], tld="co.in", num=1, stop=1, pause=2):
                url = j

                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

                r = requests.get(url, headers=headers)
                soup = BeautifulSoup(r.text, 'lxml')

                result = soup.find('article')

                #f = open("result.txt", "a")
                #f.write(result.text)
                #f.close()

    f = open('result.txt', 'r+')
    result = f.read()
    #f.truncate(0)

    return result

