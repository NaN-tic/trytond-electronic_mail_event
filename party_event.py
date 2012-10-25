#This file is part electronic_mail_event module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['PartyEvent']
__metaclass__ = PoolMeta

class PartyEvent:
    'Party Event'
    __name__ = 'party.event'

    @classmethod
    def get_resource(cls):
        res = super(PartyEvent, cls).get_resource()
        Model = Pool().get('ir.model')
        model_ids = Model.search([
            ('model', '=', 'electronic.mail'),
            ])
        for model in Model.browse(model_ids):
            res.append([model.model, model.name])
        return res

