# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Pet Adoption',
    'version': '1.0.0',
    'category': 'Pet',
    'author': 'David',
    'sequence': -15,  # Position in screen negative number means 1st
    'summary': 'Pet Adoption',
    'description': """
        Pet Adoption
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'data/adopter_data.xml',
        'data/pet_data.xml',
        # 'data/sales_order_data.xml',
        'data/sequence_data.xml',
        'views/menu.xml',
        'views/adopter_view.xml',
        'views/pet_view.xml',
        'views/adoption_order_view.xml'
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}
