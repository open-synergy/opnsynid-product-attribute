# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ec_number_id = fields.Many2one(
        string="EC Number",
        comodel_name="product.ec_number",
    )
