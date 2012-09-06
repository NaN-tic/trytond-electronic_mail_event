#This file is part electronic_mail_event module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields

class Template(ModelSQL, ModelView):
    _name = 'electronic.mail.template'

    party = fields.Char('Party',
        help='Party ID who an email event is logged. Placeholders can be used here. eg. ${record.party.id}')

Template()
