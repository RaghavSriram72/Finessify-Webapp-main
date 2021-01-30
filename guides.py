try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

from bs4 import BeautifulSoup
import requests
import os
import urllib.parse

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

            f = open("result.txt", "a")
            f.write(result.text)
            f.close()

f = open('result.txt', 'r+')
print(f.read())
f.truncate(0)
