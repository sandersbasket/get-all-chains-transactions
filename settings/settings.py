import json 

with open("./settings/config.json", "r") as file:
    config: dict = json.loads(file.read())