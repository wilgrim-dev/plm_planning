# -*- coding: utf-8 -*-
{
    'name': "PLM Planning",
    'summary': """PLM Module""",
    'description': """
        This module/app will be used for planning.
    """,

    'author': "Wilson Ndirangu",
    'website': "https://www.odoo.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product Lifecycle Management (PLM)',
    'version': '16.0.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        # 'data/sequence.xml',
        'views/planning.xml',
        'views/plm_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets': {
       'web.assets_backend': [
        ],
       'web.assets_qweb': [
       ],
    },
    'external_dependencies': {'python': [
    ]},
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}

