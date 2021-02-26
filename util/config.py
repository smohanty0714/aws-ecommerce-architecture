"""
    Load the configuration from /configs/config.json
"""

from json import loads


def load_config():
    try:
        with open('configs/config.json', 'r') as config_file:
            config_json = config_file.read().replace('\n', '')
        config_dict = loads(config_json)
    except FileNotFoundError:
        config_dict = None

    return config_dict



