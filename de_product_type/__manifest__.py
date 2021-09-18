# -*- coding: utf-8 -*-
{
    'name': "de_product_type",

    'summary': """
        Removes the option of Consumable Product from Product Type""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dynexcel ",
    'website': "http://www.dynexcel.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Product',
    'version': '11.0',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}