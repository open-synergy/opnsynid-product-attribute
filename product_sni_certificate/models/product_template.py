# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from datetime import datetime

_SNI_STATE = [
    ('certified', 'Certified'),
    ('not_certified', 'Not Certified')
]


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    @api.depends(
        "sni_ids",
        "sni_ids.name",
        "sni_ids.date_start",
        "sni_ids.date_end",
    )
    def _compute_sni_state(self):
        date_now = datetime.now().strftime("%Y-%m-%d")
        for product in self:
            if isinstance(product.id, models.NewId):
                continue
            product.sni_id = False
            if product.sni_ids:
                sni = product.sni_ids[0]
                if not sni.date_end:
                    product.sni_state = "certified"
                    product.sni_id = sni
                else:
                    if sni.date_end > date_now:
                        product.sni_state = "certified"
                        product.sni_id = sni
                    else:
                        product.sni_state = "not_certified"
            else:
                product.sni_state = "not_certified"

    sni_ids = fields.One2many(
        string="Product SNI",
        comodel_name="product.sni",
        inverse_name="product_tmpl_id"
    )
    sni_id = fields.Many2one(
        string="Active SNI Certificate",
        comodel_name="product.sni",
        compute="_compute_sni_state",
    )
    sni_state = fields.Selection(
        string="SNI Status",
        compute="_compute_sni_state",
        selection=_SNI_STATE,
        store=True
    )
