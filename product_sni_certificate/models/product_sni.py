# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductSNI(models.Model):
    _name = "product.sni"
    _inherit = "product.certificate"
    _description = "Product SNI"

    standar_sni_id = fields.Many2one(
        string="Standar SNI",
        comodel_name="product.standar_sni"
    )
