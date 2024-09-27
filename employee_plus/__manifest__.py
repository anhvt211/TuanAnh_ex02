# -*- coding: utf-8 -*-
{
    'name': "Employee PlusZZ",
    'summary': """Employee Plus""",
    'description': """Employee Plus""",
    'category': 'Uncategorized',
    'website': "https://aum.vn",
    'author': 'TA',
    'version': '1.0',
    'depends': [
        'base', 'hr', 'web'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'wizard/experience_wizard.xml',
        'views/employee_plus.xml',
        # 'views/templates.xml',
        'wizard/employee_mass_update_wizard.xml'
    ],
    'assets': {
        # "web.assets_backend":[
        #     'web/static/src/xml/**/*',
        # ],
        'web.assets_backend': [
                'employee_plus/static/src/js/bold.js',
            ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
