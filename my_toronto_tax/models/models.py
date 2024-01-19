# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta


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

class dateDeadLine(models.Model):
  _inherit = "project.task"

  computed_deadline = fields.Boolean("Deadline Auto-Computed?")
  days_shifted = fields.Integer(string='Shifted Days:', default=1)
  shifted_counts = fields.Selection([('day','Days')], default='day')
  date_deadline = fields.Date(string='Deadline', index=True, copy=False, tracking=True, task_dependency_tracking=True, compute='_compute_date_deadline')

  @api.depends('computed_deadline')
  def _compute_date_deadline(self):
    for task in self:
      if task.computed_deadline:
        task.date_deadline = task.create_date + timedelta(days=task.days_shifted)
      else:
        task.date_deadline = task.date_deadline