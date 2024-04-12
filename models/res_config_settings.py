from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """Inherited a new field into pos settings"""
    _inherit = 'res.config.settings'

    product_quantity_loc_id = fields.Many2one('stock.location',
                                              string='Product Location',
                                              config_parameter=
                                              'pos_quantity.'
                                              'product_quantity_loc_id',
                                              help='Choose Product Location',
                                              readonly=False)
