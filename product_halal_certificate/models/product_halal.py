# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class ProductHalal(models.Model):
    _name = "product.halal"
    _inherit = "product.certificate"
    _description = "Product Halal"
