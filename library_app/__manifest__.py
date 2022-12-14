# -*- coding: utf-8 -*-
{
    'name': "library_app",

    'summary': """
        Aplicación para el manejo de libros de una biblioteca""",

    'description': """
        Descripción larga del módulo
    """,

    'author': "Walter Donda",
    'website': "https://github.com/walterdonda/library",

    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Library',
    'version': '15.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         'security/library_security_groups.xml',
         'security/ir.model.access.csv',
         'views/book_view.xml',
         'views/library_menu.xml',
         'views/book_list_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
