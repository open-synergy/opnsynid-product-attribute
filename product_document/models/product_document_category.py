# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import models, fields


class ProductDocumentCategory(models.Model):
    _name = "product.document.category"
    _description = "Product Document Category"
    _order = "name"

    code = fields.Char(
        string="Code",
        required=True
    )
    name = fields.Char(
        string="Document Category",
        required=True,
        translate=True
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
    note = fields.Text(
        string="Note",
    )
