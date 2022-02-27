# -*- coding: utf-8 -*-
{
    'name': "Incidencias",

    'summary': """
        Módulo de incidencias""",

    'description': """
        Registro de la incidencias en los municipios de Gran Canaria.
    """,

    'author': "Ruben",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project', 'mail'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/municipios_report.xml',
        'reports/municipios_report_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application':True,
}
