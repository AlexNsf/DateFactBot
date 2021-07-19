import json
import os

cur_path = os.path.dirname(os.path.abspath(__file__))

secrets_file = cur_path + "\configs\secrets.json"


def load_secrets(secrets_file_name):
    with open(secrets_file_name, 'r', encoding="utf-8") as config_file:
        res = json.loads(config_file.read())
        return res


secrets = load_secrets(secrets_file)
