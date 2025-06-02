import json

DATA_FILE = 'users.json'

def read_users():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

