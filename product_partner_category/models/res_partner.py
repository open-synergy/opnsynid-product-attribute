# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    product_categ_ids = fields.Many2many(
        string="Product Categories",
        comodel_name="product.category",
        relation="rel_partner_2_product",
        column1="partner_id",
        column2="product_categ_id",
    )
