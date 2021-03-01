# TASK 1: Elasticsearch Import Script
## Introduction
This script provides interface for getting JSON format data into [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html). 

The script requires Python. It was written in Python 3.7. This project provides a requirements.txt file for easily installing dependencies using pip. It is generally a good practice to use [virtualenv](https://virtualenv.pypa.io/en/stable/) in Python 3.7 to setup a separate Python environment for installing binaries to prevent conflicts among dependencies.

This script's dependencies can be installed by running the following command from within the project folder:
```
pip -r requirements.txt
```
pip will install ```elasticsearch``` and ```requests```
### Elasticsearch
This script requires a running and reachable instance of Elasticsearch. Use the ```docker-compose.yml``` file which will help you to quickly setup a local dev environment with ElasticSearch and Kibana. When compose finishes, verify that ElasticSearch is running at: http://localhost:9200. You can also access Kibana at: http://localhost:5601/app/dev_tools#/console.
 
Define the domain name or IP address for Elasticsearch in the config json in ```\config\config.json``` before running the script. 
## Usage
The script will read a JSON file and post the data into Elasticsearch.

```
usage: python es-load.py --help
usage: es-load.py [jsonFile] [esIndex]
example : es-load.py python es_load.py data/causaly_be_mock_data.ndjson articles

Read a data from JSON file and post the data to ElasticSearch

positional arguments:
  jsonFile    Path to JSON file to read
  esIndex     Name of the ElasticSearch index mapping

optional arguments:
  -h, --help  show this help message and exit
```
