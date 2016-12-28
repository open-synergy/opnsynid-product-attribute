# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductICSSNI(models.Model):
    _name = "product.ics_sni"
    _description = "Product ICS SNI"

    name = fields.Char(
        string="ICS"
    )
    description = fields.Text(
        string="Description"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
