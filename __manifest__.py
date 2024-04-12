{
    'name': 'POS Quantity',
    'version': '17.0.1.0.0',
    'description': 'Product Available Quantity in POS',
    'category': 'Point of Sale/POS Quantity',
    'summary': 'Product Available Quantity in shown in Product card',
    'installable': True,
    'application': True,
    'depends': [
        'base',
        'point_of_sale',
        ],
    'data': [
        'views/pos_settings_views.xml',
        'views/product_views.xml',
    ],
    'assets':{
            'point_of_sale._assets_pos':[
                '/pos_quantity/static/src/xml/product_widget_views.xml',
                '/pos_quantity/static/src/xml/product_card.xml',

            ]
    }
}