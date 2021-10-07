# -*- coding: utf-8 -*-
from odoo import fields, models


class StockPickingExt(models.Model):
    _inherit = 'stock.picking'

    claim_id = fields.Many2one('sale.claim', string='Claim')
