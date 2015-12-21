var editor = new JSONEditor(document.getElementById('editor_holder'),{
    schema: {'properties': {
                'billing_address': {
                    'properties': {
                        'postal_code': {
                            'propertyOrder': 1,
                            'title': 'Postal code',
                            'type': 'string'},
                        'street': {
                            'propertyOrder': 0,
                            'title': 'Street',
                            'type': 'string'}},
                        'propertyOrder': 1,
                        'required': [],
                        'title': 'Billing address',
                        'type': 'object'},
                'delevery_address': {
                    'properties': {
                        'postal_code': {
                            'propertyOrder': 1,
                            'title': 'Postal code',
                            'type': 'string'},
                        'street': {
                            'propertyOrder': 0,
                            'title': 'Street',
                            'type': 'string'}},
                    'propertyOrder': 3,
                    'required': [],
                    'title': 'Delevery address',
                    'type': 'object'},
                'firstname': {
                    'propertyOrder': 4,
                    'title': 'Firstname',
                    'type': 'string'},
                'lastname': {
                    'propertyOrder': 0,
                    'title': 'test',
                    'type': 'string'},
                'other_addresses': {
                    'items': {
                        'properties': {
                            'postal_code': {
                                'propertyOrder': 1,
                                'title': 'Postal code',
                                'type': 'string'},
                            'street': {
                                'propertyOrder': 0,
                                'title': 'Street',
                                'type': 'string'}},
                        'required': [],
                        'type': 'object'},
                    'propertyOrder': 2,
                    'title': 'Other addresses',
                    'type': 'array'}},
                'required': [],
                'title': 'Person',
                'type': 'object'},
    theme: 'bootstrap2'
});
var editor = new JSONEditor(document.getElementById('editor_holder'),{
    schema: {'properties': {
                'articles_id': {
                    'items': {
                        'properties': {
                            'name': {
                                'propertyOrder': 1,
                                'title': 'Name',
                                'type': 'string'},
                            'number': {
                                'propertyOrder': 2,
                                'title': 'Number',
                                'type': 'integer'},
                            'price': {
                                'propertyOrder': 0,
                                'title': 'Price',
                                'type': 'integer'}},
                            'required': [],
                            'type': 'object'},
                            'propertyOrder': 0,
                            'title': 'Articles',
                            'type': 'array'},
                'price': {
                    'propertyOrder': 1,
                    'title': 'Price',
                    'type': 'integer'},
                'uuid_order': {
                    'propertyOrder': 2,
                    'title': 'Order',
                    'type': 'string'}},
                'required': ['articles_id'],
                'title': 'Order',
                'type': 'object'},
    theme: 'bootstrap2'
});