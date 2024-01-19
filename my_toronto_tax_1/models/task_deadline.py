# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import timedelta, datetime, time

class TaskDeadLine(models.Model):
    _inherit = "project.task"

    is_computed_deadline = fields.Boolean("Deadline Auto-Computed?")
    days_shifted = fields.Integer(string='Shifted Days', default=1)
    shifted_unit = fields.Selection([
        ('day', 'Days')
    ], default='day')
    date_deadline = fields.Date(string='Deadline', index=True, copy=False, tracking=True, task_dependency_tracking=True, compute='_compute_set_date_deadline')
    # date_deadline = fields.Date(string='Deadline', index=True, copy=False, tracking=True, task_dependency_tracking=True)

    @api.onchange("days_shifted")
    @api.depends('is_computed_deadline')
    def _compute_set_date_deadline(self):
        for task in self:
            if task.is_computed_deadline:
                task.date_deadline = task.create_date + timedelta(days=task.days_shifted)
            else:
                task.date_deadline = task.date_deadline

