var editor = new JSONEditor(document.getElementById('editor_holder'),{
    schema: {'properties': {
                'billing_address': {
                    'properties': {
                        'postal_code': {
                            'title': 'postal_code',
                            'type': 'string'
                        },
                        'street': {
                            'title': 'street',
                            'type': 'string'}
                        },
                        'required': [],
                        'type': 'object'},
                'delevery_address': {
                    'properties': {
                        'postal_code': {
                            'title': 'postal_code',
                            'type': 'string'
                        },
                        'street': {
                            'title': 'street',
                            'type': 'string'}
                        },
                        'required': [],
                        'type': 'object'},
                'firstname': {
                    'title': 'firstname', 
                    'type': 'string'
                },
                'lastname': {
                    'title': 'lastname', 
                    'type': 'string'
                },
                'other_addresses': {
                    'items': {
                        'properties': {
                            'postal_code': {
                                'title': 'postal_code',
                                'type': 'string'
                            },
                            'street': {
                                'title': 'street',
                                'type': 'string'}
                            },
                            'required': [],
                            'type': 'object'},
                        'type': 'array'}
                    },
            'required': [],
            'title': 'Person',
            'type': 'object'},
    theme: 'bootstrap2'
});
var editor = new JSONEditor(document.getElementById('editor_holder'),{
    schema: {'properties': {
                'articles': {
                    'items': {
                        'properties': {
                            'name': {
                                'title': 'name',
                                'type': 'string'
                            },
                            'number': {
                                'title': 'number',
                                'type': 'integer'
                            },
                            'price': {
                                'title': 'price',
                                'type': 'integer'
                            }
                        },
                        'required': [],
                        'type': 'object'},
                    'type': 'array'},
                'price': {
                    'title': 'price', 
                    'type': 'integer'}
                },
            'required': ['articles'],
            'title': 'Order',
            'type': 'object'
        },
    theme: 'bootstrap2'
});