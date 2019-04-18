# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import models, fields


class ProductDocument(models.Model):
    _name = "product.document"
    _description = "Product Document"
    _order = "name"

    name = fields.Char(
        string="# Document",
        required=True
    )
    category_id = fields.Many2one(
        string="Category",
        required=True,
        comodel_name="product.document.category"
    )
    product_tmpl_id = fields.Many2one(
        string="Product",
        required=True,
        comodel_name="product.template",
        ondelete="cascade"
    )
    partner_issued_id = fields.Many2one(
        string="Issued by",
        comodel_name="res.partner"
    )
    place_issuance = fields.Char(
        string="Place of Issuance"
    )
    date_issued = fields.Date(
        string="Issued on"
    )
    valid_from = fields.Date(
        string="Valid from"
    )
    valid_until = fields.Date(
        string="Valid until"
    )
    comment = fields.Text(
        string="Notes"
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "New"),
            ("open", "Running"),
            ("pending", "To Renew"),
            ("close", "Expired"),
        ],
        default="draft",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
