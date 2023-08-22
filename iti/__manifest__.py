# -*- coding: utf-8 -*-
{
    'name': "iti",
    'sequence': -100,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'reports/iti_student_template.xml',
        'reports/iti_student_report_templets.xml',
    'security/iti_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/iti_student_view.xml',
        'views/iti_track_view.xml',

    ],

    'application': True,
}