# -*- coding: utf-8 -*-

import datetime
import uuid
import decimal

from copy import deepcopy
from marshmallow import fields, missing


TYPE_MAP = {
    dict: {
        'type': 'object',
    },
    list: {
        'type': 'array',
    },
    datetime.time: {
        'type': 'string',
        'format': 'time',
    },
    datetime.timedelta: {
        # TODO explore using 'range'?
        'type': 'string',
    },
    datetime.datetime: {
        'type': 'string',
        'format': 'date-time',
    },
    datetime.date: {
        'type': 'string',
        'format': 'date',
    },
    uuid.UUID: {
        'type': 'string',
    },
    str: {
        'type': 'string',
    },
    bytes: {
        'type': 'string',
    },
    decimal.Decimal: {
        'type': 'number',
    },
    set: {
        'type': 'array',
    },
    tuple: {
        'type': 'array',
    },
    float: {
        'type': 'number',
    },
    int: {
        'type': 'integer',
    },
    bool: {
        'type': 'boolean',
    },
}


def to_title(attribute, ignore_list=['uuid', 'id']):
    title = " ".join([attr for attr in attribute.split('_') if attr not in ignore_list])
    return title.capitalize()


def dict_merge(a, b):
    if not isinstance(b, dict):
        return b
    result = deepcopy(a)
    for k, v in b.items():
        if k in result and isinstance(result[k], dict):
            result[k] = dict_merge(result[k], v)
        else:
            result[k] = deepcopy(v)
    return result


def dump_schema(schema_obj, recursive=None):
    json_schema = {
        "type": "object",
        "properties": {},
        "required": [],
    }
    mapping = {v: k for k, v in schema_obj.TYPE_MAPPING.items()}
    mapping[fields.Email] = str
    mapping[fields.Dict] = dict
    mapping[fields.List] = list
    mapping[fields.Url] = str
    mapping[fields.LocalDateTime] = datetime.datetime
    if not recursive :
        json_schema['title'] = schema_obj.__class__.__name__
    for position, (field_name, field) in enumerate(schema_obj.fields.items()):
        if isinstance(field, fields.Nested):
            if field.many:
                sub_json_schema = dump_schema(field.schema, recursive=True)
                json_schema['properties'][field_name] = {}
                json_schema['properties'][field_name]['type'] = 'array'
                json_schema['properties'][field_name]['items'] = sub_json_schema
            else:
                sub_json_schema = dump_schema(field.schema, recursive=True)
                json_schema['properties'][field_name] = sub_json_schema
        else:
            python_type = mapping[field.__class__]
            json_schema['properties'][field.name] = {}         
            for key, val in TYPE_MAP[python_type].items():
                json_schema['properties'][field.name][key] = val
        json_schema['properties'][field_name]['propertyOrder'] = position
        json_schema['properties'][field_name]['title'] = to_title(field_name)

        if field.default is not missing:
            json_schema['properties'][field.name]['default'] = field.default
        if field.required:
            json_schema['required'].append(field.name)
        if field.metadata and 'metadata' in field.metadata:
            if 'json_schema' in field.metadata['metadata']:
                json_schema['properties'][field_name] = dict_merge(json_schema['properties'][field_name], 
                                                                   field.metadata['metadata']['json_schema'])
    return json_schema
