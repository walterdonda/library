# -*- coding: utf-8 -*-
{
    'name': "library_member",

    'summary': """
        Este módulo extiende la app library_app para poder manejar a los miembros de la librería""",

    'author': "Walter Oscar Donda",
    'website': "http://www.yourcompany.com",

    # any module necessary for this one to work correctly
    'depends': ['base','library_app','mail'],

    # always loaded
    'data': [
        "security/library_security_groups.xml",
        "security/ir.model.access.csv",
        'views/book_view.xml',
        'views/member_view.xml',
        'views/templates.xml',
        'views/library_menu.xml',
        'views/res_partner.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
