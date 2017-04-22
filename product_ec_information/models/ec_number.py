# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class EcNumber(models.Model):
    _name = "product.ec_number"
    _description = "EC Number"

    name = fields.Char(
        string="EC Number",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    category_id = fields.Many2one(
        string="Category",
        comodel_name="product.ec_number_category",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    description = fields.Text(
        string="Description",
    )
