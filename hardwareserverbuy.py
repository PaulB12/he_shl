import requests
import time
from bs4 import BeautifulSoup

global s
acc = int(input("Enter the bankacc number: "))
PHPSESS = input("Enter the PHPSESSID: ")
s = requests.Session()
s.cookies.update ({
        "PHPSESSID" : PHPSESS,
})
s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"})
def buyExternalHD(amount,acc):
    print("Buying ",amount," new server")
    print(acc)
    while amount > 0:
        hfix3 = "https://legacy.hackerexperience.com/hardware?opt=buy" #he likes to be odd
        s.get(hfix3)
        payload = {
            'acc':str(acc),
            'price':'10000000',
            'act':'BUY-PC'
        }
        s.post(hfix3,payload)
        print("Bought a new sever")
        amount = amount - 1


amount = int(input("Enter the amount of money you wish to spend on server's: "))
NoS = amount / 10000000
NoS = int(NoS)
if NoS <= 0:
    print("You do not have enough money!")
else:
    buyExternalHD(NoS,acc)
             


