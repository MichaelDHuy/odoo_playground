# -*- coding: utf-8 -*-

from odoo import models, fields, api


class my_toronto_tax(models.Model):
    _name = 'my_toronto_tax.my_toronto_tax'
    _description = 'my_toronto_tax.my_toronto_tax'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


