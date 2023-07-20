{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'description': """AttributeErrorMotorcycle Registry 
    ====================
    This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    'author': 'ksgv-odoo',
    'website': 'https://github.com/ksgv-odoo',
    'category': 'Kawiil/Kawiil',
    'license': 'OPL-1',

    'depends': ['base'],
    'data':[
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        'security/registry_security.xml',
    ],
    'demo': [
        'demo/registry_demo.xml',
    ],
    'application':True
}   