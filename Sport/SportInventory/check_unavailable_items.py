import time
from datetime import datetime
import requests
import json
import os

BASE_URL = 'http://127.0.0.1:8000/equipment/unavailable/'

def get_unavailable_items():
    # This Function will create a json file for empty items
    try:

        response = requests.get(BASE_URL)
        if response.status_code == 200:
            items = response.json()
            if items:
                time_stamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                directory = 'unavailable_items'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                filename = os.path.join(directory, f'unavailable_items_{time_stamp}.json')

                with open(filename, 'w') as f:
                    json.dump(items, f, indent=4)
                    print("File created")
        else:
            print("Error fetching unavailable items")
    except Exception as e:
        print(f"Caught Exception while fetching Data i.e. {e}")

while True:
    get_unavailable_items()
    time.sleep(60)
