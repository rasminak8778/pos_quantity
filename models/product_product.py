# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_quant = fields.Float(string='Product Available Quant',
                                 compute='_compute_product_quant')

    def _compute_product_quant(self):
        """function for calculating product quant based on location chosen
        in pos settings"""

        for rec in self:
            print('h')
            rec.product_quant = 0
            location_setting = rec.env['ir.config_parameter'].sudo().get_param(
                'pos_quantity.product_quantity_loc_id')
            print('location_settings', location_setting)
            location = rec.env['stock.quant'].search(
                [('location_id', '=', int(location_setting)),
                 ('product_id', '=', rec.id)])
            print('location', location)
            rec.product_quant = sum(location.mapped('quantity'))
            # for loc in location:
            #     rec.product_quant += loc.quantity
