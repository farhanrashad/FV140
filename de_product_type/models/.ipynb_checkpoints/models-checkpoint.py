from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    type = fields.Selection([
        ('service', 'Service'),
        ('product', 'Stockable Product'),
    ], string='Product Type', index=True, copy=False, default='product', required=True, track_visibility='onchange')