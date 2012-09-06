#This file is part electronic_mail_event module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool

class PartyEvent(ModelSQL, ModelView):
    'Party Event'
    _name = 'party.event'

    def get_resource(self):
        res = super(PartyEvent, self).get_resource()
        model_obj = Pool().get('ir.model')
        model_ids = model_obj.search([
            ('model', '=', 'electronic.mail'),
            ])
        for model in model_obj.browse(model_ids):
            res.append([model.model, model.name])
        return res

PartyEvent()
