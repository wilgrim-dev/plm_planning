# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

import logging

_logger = logging.getLogger(__name__)


class Planning(models.Model):
    _name = 'plm.planning'
    _description = "PLM Planning Module"
    _order = "valid_from desc"
    _rec_name = "valid_from"

    valid_from = fields.Date('Valid From')
    valid_to = fields.Date('Valid To')
    electric_units = fields.Float('Electricity Units', default=0.0)
    water_units = fields.Float('Water Units', default=0.0)
    broiler_operator = fields.Integer('Broiler Operator(s)')
    raw_operator = fields.Integer('Raw Material Operator(s)')
    total_operator = fields.Integer(compute='_compute_total_operators', readonly=True)
    drying_speed = fields.Float('Max Speed Drying')
    nominal_speed = fields.Float('Nonimal Speed')
    output = fields.Char() #TODO: more details required for computing
    active = fields.Boolean(default=True)

    @api.depends('broiler_operator', 'raw_operator')
    def _compute_total_operators(self):
        for rec in self:
            rec.total_operator = rec.broiler_operator + rec.raw_operator    