import requests
import random
import os

def main():
    humid = random.randint(60,90)
    temp = random.randint(0,10)
    D = str({"humid": humid, "station": 666, "temp": temp}).encode('utf-8')
    H = {'Content-Type': "application/json",
         'Accept': "application/vnd.pagerduty+json;version=2"}
    P = requests.put(url+'/reg', data=D, header=H)

if __name__ == '__main__':
    main()
