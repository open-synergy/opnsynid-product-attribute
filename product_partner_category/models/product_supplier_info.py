# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProductSupplierinfo(models.Model):
    _inherit = "product.supplierinfo"

    @api.multi
    @api.depends(
        "name")
    def _compute_allowed_categ_ids(self):
        for prod in self:
            prod.allowed_categ_ids = [(6, 0, prod.name.product_categ_ids.ids)]

    allowed_categ_ids = fields.Many2many(
        string="Allowed Product Categories",
        comodel_name="product.category",
        compute="_compute_allowed_categ_ids",
        store=False,
    )
    categ_id = fields.Many2one(
        string="Product Category",
        comodel_name="product.category",
    )

    @api.onchange("name")
    def onchange_categ_id(self):
        self.categ_id = False
