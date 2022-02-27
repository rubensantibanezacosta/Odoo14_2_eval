# -*- coding: utf-8 -*-
# Part of AktivSoftware See LICENSE file for full copyright
# and licensing details.
{
    'name': "Reports with Watermark 1.0",
    'summary': """
            Generates reports with watermark as per the image uploaded.
             """,
    'description': """
        The module mainly works with the functionality of ading
        watermark to all pdf reports in Odoo.
    """,
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'version': '14.0.1.0.0',
    'depends': ['web', 'sale_management', 'purchase'],
    'data': [
        'views/res_company_views.xml',
        'report/external_layout_template.xml',
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'auto_install': False,
    'installable': True,
    'application': False
}
