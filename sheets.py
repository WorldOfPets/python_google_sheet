import requests
from bs4 import BeautifulSoup as bs
import sched, time
import smtplib

from email.mime.text import MIMEText
s = sched.scheduler(time.time, time.sleep)

def read(sc):
    
    response = requests.get("https://docs.google.com/spreadsheets/d/1ULczcQ1kMnUJlCK5FPK6BJ-Q2whkGoNUnKnzIC9maGU/edit?usp=sharing")
    respon = requests.get("https://docs.google.com/spreadsheets/d/1ULczcQ1kMnUJlCK5FPK6BJ-Q2whkGoNUnKnzIC9maGU/edit?usp=sharing")
    assert respon.status_code == 200, "Wrong status code"
    soup = bs(respon.content)
    tds = soup.find_all('td')
    csv_data = []

    for td in tds:
        inner_text = td.text
        strings = inner_text.split("\n")
        if not str(strings).startswith("Возм"):
            #sv_data.append(strings)
            csv_data.extend([string for string in strings if string])
    arr_str = ",".join(csv_data)
    arr = arr_str.split(",")
    for i in arr:
        if str(i).find("Воз") or str(i).find("исключительно"):
            print(i)
    
    sc.enter(60, 1, read, (sc,))

s.enter(10, 1, read, (s,))
s.run()