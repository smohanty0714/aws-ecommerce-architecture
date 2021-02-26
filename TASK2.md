## TASK 2
Find the below query that will address the TASK-2, to achieve the requirement :
 1. `It does not matter how many times you find the word "coffee" in the title, abstract
or tags attributes. You should only score on the first match.`  

There is a need of small index change to disable the [Term Frequency](https://www.elastic.co/guide/en/elasticsearch/guide/current/scoring-theory.html#tf) , by adding the ` "index_options": "docs"` to the fields.

### Query:
```
{
  "query": {
    "bool": {
      "should": [
        {
          "nested": {
            "path": "relationships",
            "query": {
              "multi_match": {
                "query": "coffee",
                "fields": [
                  "relationships.cause_concept_name"
                ]
              }
            }
          }
        },
        {
          "multi_match": {
            "query": "coffee",
            "fields": [
              "title^1",
              "tags^0.51",
              "abstract^0.1"
            ]
          }
        }
      ]
    }
  }
}
```
### Index:

```
{
  "mappings": {
    "properties": {
      "uuid": {
        "type": "keyword",
        "ignore_above": 256,
        "normalizer": "to_lowercase"
      },
      "title": {
        "type": "text",
        "analyzer": "standard",
				"index_options": "docs"
      },
      "abstract": {
        "type": "text",
        "analyzer": "standard",
				"index_options": "docs"
      },
      "tags": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256,
            "normalizer": "to_lowercase",
						"index_options": "docs"
          }
        },
        "analyzer": "standard"
      },
      "relationships": {
        "type": "nested",
        "properties": {
          "cause_concept_name": {
            "type": "keyword",
            "ignore_above": 256,
            "normalizer": "to_lowercase"
          },
          "effect_concept_name": {
            "type": "keyword",
            "ignore_above": 256,
            "normalizer": "to_lowercase"
          }
        }
      }
    }
  },
  "settings": {
    "index": {
      "analysis": {
        "normalizer": {
          "to_lowercase": {
            "filter": [
              "lowercase"
            ],
            "type": "custom"
          }
        }
      }
    }
  }
}

```