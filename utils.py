import json

def parse_config(config_path):
    with open(config_path, 'r') as file:
        cfg = json.loads(file)

    return cfg

    