# -*- coding: utf-8 -*-
{
    'name': "plan d'amelioration",

    'summary': """
        Plan d'amelioration de metro d'alger""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Massi & Farid",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'plan',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','contacts','report_xlsx'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/plan_direction_view.xml',
        'views/plan_employe_view.xml',
        'views/plan_processus_view.xml',
        'views/plan_unite_view.xml',
        'views/plan_constat_view.xml',
        'views/plan_action_view.xml',
        'views/plan_affectation_pilote_view.xml',
        'data/affectation_pilote_mail.xml',
        'data/pilote_affecte_mail.xml',
        'data/action_date_fin_notification.xml',
        'data/send_date_fin_action_mail.xml',
        'data/redefinition_action_mail.xml',
        'data/action_valide.xml',
        'data/action_corrective_approuve.xml',
        'data/action_approuve.xml',
        'report/constat_report.xml',
        'report/constat_report_template.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
