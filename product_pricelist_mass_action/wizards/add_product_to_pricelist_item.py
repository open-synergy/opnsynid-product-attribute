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
        products = self.product_ids
        criteria = [
            ("price_version_id", "=", self.price_version_id.id),
            ("product_tmpl_id", "=", False),
            ("categ_id", "=", False),
        ]
        existing_products = obj_item.search(
            criteria).mapped("product_id")
        add_products = products - existing_products
        update_products = products & existing_products

        for product in add_products:
            data = self._prepare_pricelist_item_data()
            data.update({"product_id": product.id})
            obj_item.create(data)

        if self.existing_data == "update":
            criteria2 = [
                ("price_version_id", "=", self.price_version_id.id),
                ("product_tmpl_id", "=", False),
                ("categ_id", "=", False),
                ("product_id", "in", update_products.ids),
            ]
            update_items = obj_item.search(criteria2)
            for product in update_items:
                data = self._prepare_pricelist_item_data()
                product.write(data)
