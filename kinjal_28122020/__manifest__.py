# -*- coding: utf-8 -*-
{
    'name': "kinjal_28122020",
    'summary': """This module will add fields in job application form""",
    'description': """This module will add fields in job application form""",
    'author': "Aktiv software",
    'website': "http://www.aktivsoftware.com",
    'category': 'application',
    'version': '13.0.1.0.0',
    'depends': ['hr_recruitment', 'website_hr_recruitment', 'sale_management'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/hr_applicant_template.xml',
        'views/hr_recruitment_views.xml',
        'views/sale_views.xml',
    ],
}
