{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Real Estate Management',
    'category': 'Real Estate',
    'author': 'Dennis Nyagah',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/agent_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
