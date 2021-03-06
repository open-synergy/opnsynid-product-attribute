# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class GhsHazardPrecautionaryStatement(models.Model):
    _name = "product.ghs_hazard_precautionary_statement"
    _description = "GHS Hazard Precautionary Statement"

    name = fields.Char(
        string="Hazard Precautionary Statement",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    description = fields.Text(
        string="Description",
    )
