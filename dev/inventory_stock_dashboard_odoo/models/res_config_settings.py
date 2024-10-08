# -*- coding: utf-8 -*-
#############################################################################

#    is still in the development stage

#############################################################################
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"
    out_of_stock = fields.Boolean(string="Out of stock",
                                  config_parameter='inventory_stock_dashboard_odoo.out_of_stock',
                                  help="Enable if out of stock")
    out_of_stock_quantity = fields.Integer(string="Quantity",
                                           config_parameter='inventory_stock_dashboard_odoo.out_of_stock_quantity',
                                           required=True,
                                           help="Set the minimum quantity for "
                                                "considering a product as out "
                                                "of stock.")
    dead_stock_bol = fields.Boolean(string="Enable dead stock",
                                    config_parameter='inventory_stock_dashboard_odoo.dead_stock_bol',
                                    help="Enable if you want to consider dead "
                                         "stock.")
    dead_stock = fields.Integer(string="Dead stock",
                                config_parameter='inventory_stock_dashboard_odoo.dead_stock',
                                required=True,
                                help="Set the threshold quantity for "
                                     "considering a product as dead stock.")
    dead_stock_type = fields.Selection(
        [('day', 'Day'), ('week', 'Week'), ('month', 'Month')],
        string="Type", default='day',
        config_parameter='inventory_stock_dashboard_odoo.dead_stock_type',
        required=True,
        help="Select the time period to determine dead stock based on product "
             "sales.")
