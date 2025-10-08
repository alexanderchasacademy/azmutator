import requests
import random
import sys
import time

def main(url, station):
    print("Mutator started!")  # <-- Ny rad
    while True:
        humid = random.randint(60, 90)
        temp = random.randint(0, 10)
        data = {
            "humid": str(humid),
            "station": str(station),
            "temp": str(temp)
        }
        print("Sending data:", data)  # <-- Ny rad
        try:
            r = requests.put(url, json=data)
            print("Response:", r.status_code, r.text)  # <-- Ny rad
        except Exception as e:
            print("Error:", e)
        time.sleep(60)  # skicka var 60:e sekund

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python mutator.py <url> [station]")
        sys.exit(1)
    url = sys.argv[1]
    station = sys.argv[2] if len(sys.argv) > 2 else "99"
    main(url, station)
