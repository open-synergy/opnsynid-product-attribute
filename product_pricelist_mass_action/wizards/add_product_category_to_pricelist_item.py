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
        categs = self.product_categ_ids
        criteria = [
            ("price_version_id", "=", self.price_version_id.id),
            ("product_tmpl_id", "=", False),
            ("product_id", "=", False),
        ]
        existing_categs = obj_item.search(
            criteria).mapped("categ_id")
        add_categs = categs - existing_categs
        update_categs = categs & existing_categs

        for categ in add_categs:
            data = self._prepare_pricelist_item_data()
            data.update({"categ_id": categ.id})
            obj_item.create(data)

        if self.existing_data == "update":
            criteria2 = [
                ("price_version_id", "=", self.price_version_id.id),
                ("product_tmpl_id", "=", False),
                ("product_id", "=", False),
                ("categ_id", "in", update_categs.ids),
            ]
            update_items = obj_item.search(criteria2)
            for item in update_items:
                data = self._prepare_pricelist_item_data()
                item.write(data)
