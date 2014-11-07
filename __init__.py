# This file is part electronic_mail_event module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .party_event import *
from .template import *


def register():
    Pool.register(
        PartyEvent,
        Template,
        module='electronic_mail_event', type_='model')
