import json

def load_event_data(filepath):
    with open(filepath, "r") as f:
        return json.load(f)