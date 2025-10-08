import requests
import random
import sys
import os
import time

def main(url, station):
    while True:
        humid = random.randint(60,90)
        temp = random.randint(0,10)
        D = f'{{"humid": "{humid}", "station": "{station}", "temp": "{temp}"}}'.encode('utf-8')
        print(D)
        H = {'Content-Type': "application/json",
             'Accept': "application/vnd.pagerduty+json;version=2"}
        P = requests.put(url+'/api/reg', data=D, headers=H)
        print(P.status_code)
        time.sleep(10)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])