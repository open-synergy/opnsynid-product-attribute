# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class AddProductToPricelistItem(models.TransientModel):
    _name = "product.add_product_to_pricelist_item"
    _inherit = "product.add_to_pricelist_item"
    _description = "Add Product To Pricelist Item"

    product_ids = fields.Many2many(
        string="Products",
        comodel_name="product.product",
        relation="rel_add_product_to_pricelist_item",
        column1="wizard_id",
        column2="product_id",
    )

    @api.multi
    def _create_pricelist_items(self):
        self.ensure_one()
        obj_item = self.env["product.pricelist.item"]
        for product in self.product_ids:
            data = self._prepare_pricelist_item_data()
            data.update({"product_id": product.id})
            obj_item.create(data)
