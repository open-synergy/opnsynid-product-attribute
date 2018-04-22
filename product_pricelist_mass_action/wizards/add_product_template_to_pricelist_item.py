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
        product_templates = self.product_tmpl_ids
        criteria = [
            ("price_version_id", "=", self.price_version_id.id),
            ("product_id", "=", False),
            ("categ_id", "=", False),
            ("sequence", "=", self.sequence),
        ]
        existing_templates = obj_item.search(
            criteria).mapped("product_tmpl_id")
        add_templates = product_templates - existing_templates
        update_templates = product_templates & existing_templates

        for template in add_templates:
            data = self._prepare_pricelist_item_data()
            data.update({"product_tmpl_id": template.id})
            obj_item.create(data)

        if self.existing_data == "update":
            criteria2 = [
                ("price_version_id", "=", self.price_version_id.id),
                ("product_id", "=", False),
                ("categ_id", "=", False),
                ("product_tmpl_id", "in", update_templates.ids),
                ("sequence", "=", self.sequence),
            ]
            update_items = obj_item.search(criteria2)
            for item in update_items:
                data = self._prepare_pricelist_item_data()
                item.write(data)
