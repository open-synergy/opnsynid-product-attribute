# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"
    _name = "product.template"

    prepaid_income_account_id = fields.Many2one(
        string="Prepaid Income Account",
        comodel_name="account.account",
        company_dependent=True,
        domain=[
            ("type", "=", "other"),
        ],
    )
    prepaid_expense_account_id = fields.Many2one(
        string="Prepaid Expense Account",
        comodel_name="account.account",
        company_dependent=True,
        domain=[
            ("type", "=", "other"),
        ],
    )
