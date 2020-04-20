# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductUomCategory(models.Model):
    _inherit = "product.uom.categ"

    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting For Approval"),
            ("valid", "Valid"),
        ],
        default="draft",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=False,
    )
