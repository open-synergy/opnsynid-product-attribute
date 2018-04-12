# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class AddProductCategoryToPricelistItem(models.TransientModel):
    _name = "product.add_product_category_to_pricelist_item"
    _inherit = "product.add_to_pricelist_item"
    _description = "Add Product Category To Pricelist Item"

    product_categ_ids = fields.Many2many(
        string="Product Categories",
        comodel_name="product.category",
        relation="rel_add_product_category_to_pricelist_item",
        column1="wizard_id",
        column2="categ_id",
    )

    @api.multi
    def _create_pricelist_items(self):
        self.ensure_one()
        obj_item = self.env["product.pricelist.item"]
        for categ in self.product_categ_ids:
            data = self._prepare_pricelist_item_data()
            data.update({"categ_id": categ.id})
            obj_item.create(data)
