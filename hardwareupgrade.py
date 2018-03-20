import requests
import time
from bs4 import BeautifulSoup


global s
global IDs
IDs = list()
acc = int(input("Enter the bank acc number: "))
PHPSESS = input("Enter the PHPSESSID: ")
s = requests.Session()
s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"})
s.cookies.update ({
        "PHPSESSID" : PHPSESS,
})


def FindHardWareID():
    hardwardURL = 'https://legacy.hackerexperience.com/hardware?opt=xhd'
    html = s.get(hardwardURL)
    html = html.text
    soup = BeautifulSoup(html, 'html.parser')
    ulclass = soup.find_all('ul', {'class': 'list'})
    for link in ulclass:
        href = link.findAll('a')
        for l in href:
            if '1 GB' in l.text:
                print("Skipping | External HD already upgraded")
            else:
                data = (l['href'])
                print(data)
                dat = data.split('&id=')[1]
                IDs.append(dat)
                
    
    
def UpgradeHardWare(acc):
    for ID in IDs:
        url = 'https://legacy.hackerexperience.com/hardware?opt=xhd&id='+ID
        s.get(url) #HE likes to be random and makes us load the page before request can go through
        hurl = 'https://legacy.hackerexperience.com/hardware'
        payload = {
            'acc':acc,
            'act':'xhd',
            'part-id':3,
            'price':500
        }
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
    
