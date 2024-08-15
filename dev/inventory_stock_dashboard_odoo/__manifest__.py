# -*- coding: utf-8 -*-
#############################################################################

#    is still in the development stage

#############################################################################
{
    'name': 'Inventory Dashboard Odoo 16',
    'version': '16.0.1.0.1',
    'category': 'Inventory',
    'summary': 'Inventory Dashboard',
    'description': "Detailed Dashboard View For Inventory",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['stock', 'base'],
    'data': ['views/style.xml',
             'views/dashboard_menus.xml',
             'views/res_config_settings_views.xml',
             ],
    'assets': {
        'web.assets_backend': [
            'inventory_stock_dashboard_odoo/static/src/css/dashboard.css',
            'inventory_stock_dashboard_odoo/static/src/js/dashboard.js',
            'inventory_stock_dashboard_odoo/static/src/js/lib/Chart.bundle.js',
            'inventory_stock_dashboard_odoo/static/src/xml/dashboard.xml'
        ],
    },
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
