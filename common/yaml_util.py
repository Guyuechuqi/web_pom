import yaml
from config.path import DATA_PATH, CONFIG_PATH


def read_yaml(file):
    yaml_path = DATA_PATH/file
    with open(yaml_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def write_yaml(file, data):
    yaml_path = DATA_PATH/file
    with open(yaml_path, "w", encoding="utf-8") as file:
        yaml.safe_dump(data, file)

def read_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)