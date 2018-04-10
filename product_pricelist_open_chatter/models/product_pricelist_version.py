# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductPricelistVersion(models.Model):
    _name = "product.pricelist.version"
    _inherit = ["mail.thread", "product.pricelist.version"]

    name = fields.Char(
        track_visibility="onchange",
    )
    date_start = fields.Date(
        track_visibility="onchange",
    )
    date_end = fields.Date(
        track_visibility="onchange",
    )
