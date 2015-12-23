# -*- coding: utf-8 -*-

import datetime
import uuid
import decimal

from copy import deepcopy
from marshmallow import fields, missing, validate


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
    """ `to_title` converts and attribute name into a humanized title.
    """
    title = " ".join([attr for attr in attribute.split('_') if attr not in ignore_list])
    return title.capitalize()


def dict_merge(a, b):
    """ `dict_merge` deep merges b into a and returns the new dict.
    """
    if not isinstance(b, dict):
        return b
    result = deepcopy(a)
    for k, v in b.items():
        if k in result and isinstance(result[k], dict):
            result[k] = dict_merge(result[k], v)
        else:
            result[k] = deepcopy(v)
    return result


def _dump_field(field):
    field_props = {}
    field_props['title'] = to_title(field.name)

    if field.default is not missing:
        field_props['default'] = field.default
    if field.validators:
        for validator in field.validators:
            if isinstance(validator, validate.Length):
                if validator.min is not None:
                    field_props['minLength'] = validator.min
                if validator.max is not None:
                    field_props['maxLength'] = validator.max
            if isinstance(validator, validate.OneOf):
                field_props['enum'] = validator.choices
                if validator.labels:
                    if 'options' not in field_props:
                        field_props['options'] = {}
                    field_props['options']['enum_titles'] = validator.labels
    if field.metadata and 'metadata' in field.metadata:
        if 'json_schema' in field.metadata['metadata']:
            field_props = dict_merge(field_props, field.metadata['metadata']['json_schema'])

    return field_props


def dump_schema(schema, title=None):
    """ dump_schema dumps schema a `marshmallow.Schema` instance into a json_schema dictionary.
    """
    json_schema = {
        "type": "object",
        "properties": {},
        "required": [],
    }
    mapping = {v: k for k, v in schema.TYPE_MAPPING.items()}
    mapping[fields.Email] = str
    mapping[fields.Dict] = dict
    mapping[fields.List] = list
    mapping[fields.Url] = str
    mapping[fields.LocalDateTime] = datetime.datetime

    def _tm(f):  # type mapping lookup
        return TYPE_MAP[mapping[f.__class__]]

    if title is not None:
        json_schema['title'] = title
    for position, (field_name, field) in enumerate(schema.fields.items()):
        json_schema['properties'][field.name] = field_props = {}
        if isinstance(field, fields.List):
            field_props['type'] = 'array'
            field_props['items'] = _dump_field(field.container).update(_tm(field.container))
        if isinstance(field, fields.Nested):
            if field.many:
                sub_json_schema = dump_schema(field.schema)
                field_props['type'] = 'array'
                field_props['items'] = sub_json_schema
            else:
                sub_json_schema = dump_schema(field.schema)
                field_props.update(sub_json_schema)
        else:
            field_props.update(_tm(field))

        field_props['propertyOrder'] = position
        if field.required:
            json_schema['required'].append(field.name)

        field_props.update(_dump_field(field))

    return json_schema
