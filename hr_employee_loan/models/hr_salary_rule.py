# -*- coding: utf-8 -*-

from odoo import models, fields

class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    struct_id = fields.Many2one('hr.payroll.structure', string="Salary Structure", required=False, ondelete='cascade')
    is_loan_payment = fields.Boolean(string='Loan Payment')
