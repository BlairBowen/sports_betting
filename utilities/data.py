import json
import requests
import datetime
import os

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_response = response.json()
        return json_response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def save_local_data(data, output_file):
    try:
        with open(output_file, "w") as json_file:
            json.dump(data, json_file, indent=2)
        print(f"Data saved to {output_file}")
    except Exception as e:
        print(f"Error saving data to JSON file: {e}")


def load_local_data(input_file):
    try:
        with open(input_file, "r") as json_file:
            data = json.loads(json_file.read())
        print(f"Data loaded from {input_file}")
    except Exception as e:
        print(f"Error loading data from JSON file: {e}")

    return data


def refresh_data(file_path, minutes=15):
    if file_path is not None:
        f = open(f"data/{file_path}", "a+")
        f.close()
        time_modified = os.path.getmtime(f"data/{file_path}")
        time_stamp = datetime.datetime.fromtimestamp(time_modified)
        print(f"last refreshed @ {time_stamp}")
    
    if file_path is None or time_stamp + datetime.timedelta(minutes=minutes) < datetime.datetime.now() or os.path.getsize(f"data/{file_path}") == 0:
        print("updating data")
        return True
    else:
        time_stamp = time_stamp + datetime.timedelta(minutes=minutes)
        print(f"avalible update @ {time_stamp}")
        return False