# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductStandarSNI(models.Model):
    _name = "product.standar_sni"
    _description = "Product Standar SNI"

    name = fields.Char(
        string="Standar SNI"
    )
    ics_sni_id = fields.Many2one(
        string="ICS",
        comodel_name="product.ics_sni"
    )
    kode_teknis_sni_id = fields.Many2one(
        string="Kode Panitia Teknis",
        comodel_name="product.kode_teknis_sni"
    )
    description = fields.Text(
        string="Description"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
