#This file is part electronic_mail_event module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
{
    'name': 'Electronic Mail Event',
    'name_ca_ES': 'Esdeveniments correu electrònic',
    'name_es_ES': 'Eventos correo electrónico',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''Add Party Event mail reference''',
    'description_ca_ES': '''Afegeix als esdeveniments de la empresa la relació amb el correu electrònic''',
    'description_es_ES': '''Añade a los eventos de la empresa la relación con el correo electrónico''',
    'depends': [
        'ir',
        'res',
        'electronic_mail_template',
        'party_event',
    ],
    'xml': [
        'template.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}
