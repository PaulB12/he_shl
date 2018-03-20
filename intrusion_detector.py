import requests
import re
from win10toast import ToastNotifier
from time import sleep
toaster = ToastNotifier()
logged = []
PHPSESSID = input("PHPSESSID >> ")
s = requests.Session()
s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"})
s.cookies.update({"PHPSESSID":PHPSESSID})
#toaster.show_toast("Breach Detected","[1.2.3.4] logged in as root",icon_path=None,duration=10)
loginRegex = "\[[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\]\slogged\sin\sas\s" # 2018-01-11 01:34 - [232.94.185.179] logged in as root
regexTerms = [loginRegex]
while True:
    try:
        getLogs = s.get("https://legacy.hackerexperience.com/log").text
        if "Hacker Experience is a browser-based hacking" in getLogs:
            print("Error: You have been logged out")
            exit()
        for reg in regexTerms:
            search = re.findall(reg, getLogs)
            if len(search) > 0:
                for result in search:
                    if result not in logged:
                        toaster.show_toast("Breach Detected",result,icon_path=None,duration=10)
                        logged.append(result)
                        print(result)
    except Exception as e:
        print("Error: "+str(e))
    sleep(1)