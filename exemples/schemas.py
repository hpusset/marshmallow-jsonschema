#!/usr/bin/env python
# -*- coding: utf-8 -*-

from marshmallow_jsonschema import dump_schema
from marshmallow import Schema, fields, pprint, validate

Schema.Meta.ordered = False


class Article(Schema):
    name = fields.String()
    price = fields.Int()
    number = fields.Int()


class Order(Schema):
    uuid_order = fields.String()
    price = fields.Int()
    articles_id = fields.Nested(Article, many=True, required=True)


class Address(Schema):
    street = fields.String()
    postal_code = fields.String()


class Person(Schema):
    NAME_CHOICES = [ 
        1,
        2,
        3,
    ]
    LABEL = [
        'Name1',
        'Name2',
        'Name2'
    ]
    firstname = fields.String(validate=validate.OneOf(NAME_CHOICES, LABEL))
    lastname = fields.String(metadata={'json_schema': {'title': 'test'}})
    billing_address = fields.Nested(Address)
    delevery_address = fields.Nested(Address)
    other_addresses = fields.Nested(Address, many=True)
    
if __name__ == "__main__":
    p = Person()
    o = Order()
    result_person = dump_schema(p)
    result_order = dump_schema(o)
    pprint(result_person)
    pprint(result_order)