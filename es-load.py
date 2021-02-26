import argparse

from util.elasticutil import ElasticUtil
from util import config

if __name__ == '__main__':

    JSON_PARSER = argparse.ArgumentParser(
        description='Read a data from JSON file and post the data to ElasticSearch'
        )
    JSON_PARSER.add_argument("jsonFile", type=str,  help="Path to JSON file to read")
    JSON_PARSER.add_argument("esIndex", type=str, help="Name of the ElasticSearch index mapping")

    # load configs
    config_data = config.load_config()
    es_util = ElasticUtil(config_data['elastic'])
    ARGS = JSON_PARSER.parse_args()

    es_util.process_json(ARGS)
