#!/usr/bin/env python
# -*- coding: utf-8 -*-

from marshmallow_jsonschema import dump_schema
from marshmallow import Schema, fields, pprint


class Article(Schema):
    name = fields.String()
    price = fields.Int()
    number = fields.Int()


class Order(Schema):
    price = fields.Int()
    articles = fields.Nested(Article, many=True, required=True)


class Address(Schema):
    street = fields.String()
    postal_code = fields.String()


class Person(Schema):
    firstname = fields.String()
    lastname = fields.String()
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