import requests
import time
from bs4 import BeautifulSoup


global s
global IDs
IDs = list()
PHPSESS = input("Enter the PHPSESSID: ")
s = requests.Session()
s.cookies.update ({
        "PHPSESSID" : PHPSESS,
})
s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"})
acc = int(input("Enter bank account: ")

def FindHardWareID():
    hardwardURL = 'https://legacy.hackerexperience.com/hardware'
    html = s.get(hardwardURL)
    html = html.text
    soup = BeautifulSoup(html, 'html.parser')
    ulclass = soup.find_all('ul', {'class': 'list'})
    for link in ulclass:
        href = link.findAll('a')
        for l in href:
            if '4 GHz' in l.text:
                print("Skipping | Server already upgraded")
            else:
                data = (l['href'])
                dat = data.split('&id=')[1]
                IDs.append(dat)
    
    
def UpgradeHardWare(acc):
    for ID in IDs:
        url = 'https://legacy.hackerexperience.com/hardware?opt=upgrade&id='+ID
        s.get(url) #HE likes to be random and makes us load the page before request can go through
        hurl = 'https://legacy.hackerexperience.com/hardware'
        payload = {
            'acc':acc,
            'act':'hdd',
            'part-id':6,
            'price':8000
        }
        s.post(hurl,payload)
        payload = {
            'acc':acc,
            'act':'cpu',
            'part-id':8,
            'price':5000
        }
        url = 'https://legacy.hackerexperience.com/hardware?opt=upgrade&id='+ID
        s.get(url) #HE likes to be random and makes us load the page before request can go through
        s.post(hurl,payload)
        print("Hardware ID: ",ID," upgraded!")

def clearLogs():
    logUrl = "https://legacy.hackerexperience.com/logEdit"
    payload = {
        'id':1,
        'log':''
    }
    response = s.post(logUrl,payload)
    newURL = response.url
    time.sleep(4)
    Log = s.get(newURL)
FindHardWareID()
UpgradeHardWare(acc)
clearLogs()
    
