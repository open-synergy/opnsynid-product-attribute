# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProductUomConversion(models.Model):
    _name = "product.uom_conversion"
    _description = "Product UoM Conversion"

    product_template_id = fields.Many2one(
        string="Product Template",
        comodel_name="product.template",
    )
    uom_categ_id = fields.Many2one(
        string="UoM Category",
        comodel_name="product.uom.categ",
        required=True,
    )
    reference_uom_id = fields.Many2one(
        string="Referece UoM",
        comodel_name="product.uom",
        required=True,
    )
    coefficient = fields.Float(
        string="Coefficient",
        required=True,
    )

    @api.onchange("uom_categ_id")
    def onchange_reference_uom_id(self):
        self.reference_uom_id = False
        if self.uom_categ_id:
            obj_uom = self.env["product.uom"]
            criteria = [
                ("category_id", "=", self.uom_categ_id.id),
                ("uom_type", "=", "reference"),
            ]
            uoms = obj_uom.search(criteria)
            if len(uoms) > 0:
                self.reference_uom_id = uoms[0].id
