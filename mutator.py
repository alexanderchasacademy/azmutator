import requests
import random
import sys
import time
import json

def main(url, station):
    while True:
        # Generera slumpvärden
        humid = random.randint(60, 90)
        temp = random.randint(0, 10)
        data = {
            "humid": humid,
            "temp": temp,
            "station": int(station),
            "source": "mutator"  # identifierar att datan kommer från mutatorn
        }

        # Logga vad som skickas
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Sending data: {data} to {url}/reg")

        # Skicka PUT-request
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url+'/reg', json=data, headers=headers)

        # Logga responsen
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Response: {response.status_code}, content: {response.text}")

        # Vänta 60 s
        time.sleep(60)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
