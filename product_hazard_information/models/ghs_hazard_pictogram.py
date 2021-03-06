# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class GhsHazardPictogram(models.Model):
    _name = "product.ghs_hazard_pictogram"
    _description = "GHS Hazard Pictoram"

    name = fields.Char(
        string="Hazard Statement",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    image = fields.Binary(
        string="Image",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    description = fields.Text(
        string="Description",
    )
