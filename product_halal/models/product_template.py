# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from datetime import datetime

_HALAL_STATE = [
    ('certified', 'Certified'),
    ('not_certified', 'Not Certified')
]


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    @api.depends(
        "halal_ids",
        "halal_ids.name",
        "halal_ids.date_start",
        "halal_ids.date_end",
    )
    def _compute_halal_state(self):
        date_now = datetime.now().strftime("%Y-%m-%d")
        for product in self:
            product.halal_id = False
            if product.halal_ids:
                halal = product.halal_ids[0]
                if not halal.date_end:
                    product.halal_state = "certified"
                    product.halal_id = halal
                else:
                    if halal.date_end > date_now:
                        product.halal_state = "certified"
                        product.halal_id = halal
                    else:
                        product.halal_state = "not_certified"
            else:
                product.halal_state = "not_certified"

    halal_ids = fields.One2many(
        string="Product Halal",
        comodel_name="product.halal",
        inverse_name="product_tmpl_id"
    )
    halal_id = fields.Many2one(
        string="Active Halal Certificate",
        comodel_name="product.halal",
        compute="_compute_halal_state",
    )
    halal_state = fields.Selection(
        string="Halal Status",
        compute="_compute_halal_state",
        selection=_HALAL_STATE,
        store=True
    )
