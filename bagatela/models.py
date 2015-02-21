import json
from jsonschema import validate


class Procurer(object):
    schema = {
        'type': 'object',
        'properties': {
            'name': {
                'type': 'string'
            },
            'url': {
                'type': 'string',
                'pattern': '^https?://\[?\w'
            },
            'procurementPageUrl': {
                'type': 'string',
                'pattern': '^https?://\[?\w'
            },
            'selectors': {
                'type': 'object',
                'properties': {
                    'title': {
                        'type': 'string',
                    },
                    'url': {
                        'type': 'string'
                    },
                    'publishDate': {
                        'type': 'string'
                    },
                    'closureDate': {
                        'type': 'string'
                    }
                },
                'required': ['title']
            }
        },
        'required': ['name', 'url', 'procurementPageUrl', 'selectors']
    }

    def __init__(self, data):
        self.data = data

    def validate(self):
        validate(self.data, self.schema)

        return self


def get_procurers():
    fd = open('./sources.json')

    return [Procurer(data=procurer).validate() for procurer in json.load(fd)]
