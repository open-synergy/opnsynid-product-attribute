# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class AddProductTemplateToPricelistItem(models.TransientModel):
    _name = "product.add_product_template_to_pricelist_item"
    _inherit = "product.add_to_pricelist_item"
    _description = "Add Product Template To Pricelist Item"

    product_tmpl_ids = fields.Many2many(
        string="Product Templates",
        comodel_name="product.template",
        relation="rel_add_product_template_to_pricelist_item",
        column1="wizard_id",
        column2="product_tmpl_id",
    )

    @api.multi
    def _create_pricelist_items(self):
        self.ensure_one()
        obj_item = self.env["product.pricelist.item"]
        for product in self.product_tmpl_ids:
            data = self._prepare_pricelist_item_data()
            data.update({"product_tmpl_id": product.id})
            obj_item.create(data)
