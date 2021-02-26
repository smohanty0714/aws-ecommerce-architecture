"""
Reading data from JSON file and posting it to ElasticSearch
"""

import sys
import json

# use the ElasticSearch client's helpers class for _bulk API
from elasticsearch import Elasticsearch, helpers


class ElasticUtil:

    def __init__(self, config):
        # load the config from config.json
        es_hosts = str(config.get('hosts')).split(",")
        max_connection = config.get('max_connection', 3)

        # declare a client instance of the Python ElasticSearch library
        # allow up to 'max_connection' in-flight upload requests in parallel
        self.client = Elasticsearch(es_hosts, maxsize=max_connection)

    def process_json(self, args):
        """
        :param args: all parameters
        :return:
        """
        json_file_path = args.jsonFile
        es_index = args.esIndex

        try:
            # the function will return a list of docs
            docs = [l.strip() for l in open(str(json_file_path), encoding="utf8", errors='ignore')]
        except IOError:
            file_not_found_message = 'No file found at %s. Please enter a valid file path.' % json_file_path
            sys.exit(file_not_found_message)
        json_doc_list = self.prepare_docs_bulk_upload(docs)
        self.send_data_to_es(json_doc_list, es_index)

    def prepare_docs_bulk_upload(self, docs):
        """
        :param docs: list of docs
        :return:
        """
        # define an empty list for the ElasticSearch docs
        doc_list = []

        # use Python's enumerate() function to iterate over list of doc strings
        for num, doc in enumerate(docs):

            # catch any JSON loads() errors
            try:
                # prevent JSONDecodeError resulting from Python uppercase boolean
                doc = doc.replace("True", "true")
                doc = doc.replace("False", "false")

                dict_doc = json.loads(doc)
                doc_list += [dict_doc]

            except json.decoder.JSONDecodeError as err:
                print("ERROR for num:", num, "-- JSONDecodeError:", err, "for doc:", doc)

        return doc_list

    def send_data_to_es(self, doc_list, es_index):
        try:
            print("\nAttempting to index the list of docs using helpers.bulk()")
            # use the helpers library's Bulk API to index list of ElasticSearch docs
            resp = helpers.bulk(
                self.client,
                doc_list,
                index=es_index
            )
            print("Successfully documents inserted: ", resp[0])

        except Exception as err:
            print("ElasticSearch helpers.bulk() ERROR:", err)
            quit()

