# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountRegisterPayments(models.TransientModel):
    _inherit = "account.register.payments"

    bank_reference = fields.Char(copy=False)
    cheque_reference = fields.Char(copy=False)
    effective_date = fields.Date('Effective Date', help='Effective date of PDC', copy=False, default=False)

    def get_payment_vals(self):
        res = super(AccountRegisterPayments, self).get_payment_vals()
        if self.payment_method_id == self.env.ref('account_check_printing.account_payment_method_check'):
            res.update({
                'check_amount_in_words': self.check_amount_in_words,
                'check_manual_sequencing': self.check_manual_sequencing,
                'effective_date': self.effective_date,
            })
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
