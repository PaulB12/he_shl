import time
from time import sleep
import requests
from bs4 import BeautifulSoup
x = True
PHPSESSID = input("Enter your PHPSESSID: ")
bankacc = input("Bank Acc Number: ")
s = requests.Session()
s.cookies.update ({
    "PHPSESSID" : PHPSESSID,
})
s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"})
def clearLog():
    url = 'https://legacy.hackerexperience.com/logEdit'
    payload = {
        'id':1,
        'log':''
    }
    r = s.post(url,payload)
    newUrl = r.url
    print(newUrl)
    time.sleep(6)
    s.get(newUrl)
    
def queueIP():
    url = 'https://legacy.hackerexperience.com/resetIP'
    payload = {
        'acc':int(bankacc)
    }
    s.post(url,payload)
    print("10 minutes untill IP reset.")
    url = 'https://legacy.hackerexperience.com/internet?ip=1.2.3.4'
    s.get(url)
    time.sleep(60*10)
    print("IP Reset queued")

def ipReset():
    url = 'https://legacy.hackerexperience.com/internet?ip=1.158.201.174'
    s.get(url)
    s.get(url)
    s.get(url)
    s.get(url)
    print("IP Resetted")
    clearLog()
    queueIP()

def checkLog():
    global x
    url = 'https://legacy.hackerexperience.com/log'
    text = s.get(url).text
    if 'logged in as root' in text:
        soup = BeautifulSoup(text, 'html.parser')
        log = soup.find("textarea", {"class": "logarea"})
        print(log.text)
        ipReset()

while x == True:
    checkLog()
    time.sleep(1)

