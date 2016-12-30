# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductKodeTeknisSNI(models.Model):
    _name = "product.kode_teknis_sni"
    _description = "Product Kode Panitia Teknis SNI"

    name = fields.Char(
        string="Kode Panitia Teknis",
        required=True
    )
    description = fields.Text(
        string="Description"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
