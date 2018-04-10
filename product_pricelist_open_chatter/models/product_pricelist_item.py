# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductPricelistItem(models.Model):
    _name = "product.pricelist.item"
    _inherit = ["mail.thread", "product.pricelist.item"]

    product_tmpl_id = fields.Many2one(
        track_visibility="onchange",
    )
    product_id = fields.Many2one(
        track_visibility="onchange",
    )
    categ_id = fields.Many2one(
        track_visibility="onchange",
    )
    product_tmpl_id = fields.Many2one(
        track_visibility="onchange",
    )
    min_quantity = fields.Float(
        track_visibility="onchange",
    )
    sequence = fields.Integer(
        track_visibility="onchange",
    )
    base = fields.Selection(
        track_visibility="onchange",
    )
    base_pricelist_id = fields.Many2one(
        track_visibility="onchange",
    )
    price_surcharge = fields.Float(
        track_visibility="onchange",
    )
    price_discount = fields.Float(
        track_visibility="onchange",
    )
    price_round = fields.Float(
        track_visibility="onchange",
    )
    price_min_margin = fields.Float(
        track_visibility="onchange",
    )
    price_max_margin = fields.Float(
        track_visibility="onchange",
    )
