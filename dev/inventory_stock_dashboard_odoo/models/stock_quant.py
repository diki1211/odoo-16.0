# -*- coding: utf-8 -*-
#############################################################################

#    is still in the development stage

#############################################################################
from odoo import api, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    @api.model
    def get_out_of_stock(self):
        """rpc method of out of stock graph
        Returns products and quantity"""
        company_id = self.env.company.id
        sett_out_stock_bool = self.env['ir.config_parameter'].sudo(). \
            get_param("inventory_stock_dashboard_odoo.out_of_stock", default="")
        sett_out_stock_quantity = self.env['ir.config_parameter'].sudo().\
            get_param("inventory_stock_dashboard_odoo.out_of_stock_quantity", default="")
        if sett_out_stock_bool == "True":
            if sett_out_stock_quantity:
                out_stock_value = int(sett_out_stock_quantity)
                query = '''select product_template.name,sum(stock_quant.quantity) from stock_quant
                 inner join product_product on stock_quant.product_id = product_product.id
                 inner join product_template on product_product.product_tmpl_id = product_template.id
                 where stock_quant.quantity < %s and stock_quant.company_id = %s group by product_template.name''' \
                        % (out_stock_value, company_id)

                self._cr.execute(query)
                result = self._cr.fetchall()
                total_quantity = []
                for record in result:
                    total_quantity.append(record[1])
                product_name = []
                for record in result:
                    product_name.append(record[0])
                value = {
                    'product_name': product_name,
                    'total_quantity': total_quantity
                }
                return value
