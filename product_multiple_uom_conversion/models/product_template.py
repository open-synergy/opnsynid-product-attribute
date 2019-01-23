# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    uom_conversion_ids = fields.One2many(
        string="UoM Conversion",
        comodel_name="product.uom_conversion",
        inverse_name="product_template_id",
    )
