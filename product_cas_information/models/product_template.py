# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    cas_registry_ids = fields.Many2many(
        string="CAS Registry",
        comodel_name="product.cas_registry",
        relation="rel_product_template_2_cas",
        col1="product_template_id",
        col2="cas_id",
    )
