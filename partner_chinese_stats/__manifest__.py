{
    'name':  "PARTNER_CHINESE_STATS",

    'summary': "MODULO QUE PERMITE VER EL SIGNO DEL HOROSCOPO CHINO",

    'description': """
ESTE MODULO EXTIENDE EL MODELO RES_PARTNER ANADIENDO LOS SIGUIENTES CAMPOS A LOS CONTACTOS:
    - FECHA DE NACIMIENTO
    - EDAD (CALCULADA AUTOMATICAMENTE)
    - SIGNO DEL HOROSCOPO CHINO (CALCULADO AUTOMATICAMENTE)
    - CODIGO DE SOCIO
    - NIVEL DE FIDELIDAD (CALCULADO AUTOMATICAMENTE)
 """,

    'author': "EMPLEADO SUFRIDOR",
    'website': "https://www.nocobrolosuficiente.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}