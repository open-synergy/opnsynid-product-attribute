# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResCompany(models.Model):
    _name = "res.company"
    _inherit = "res.company"

    product_category_confirm_grp_ids = fields.Many2many(
        string="Allow To Confirm Category",
        comodel_name="res.groups",
        relation="rel_company_id_confirm",
        column1="company_id",
        column2="group_id",
    )
    product_category_valid_grp_ids = fields.Many2many(
        string="Allow To Validate Category",
        comodel_name="res.groups",
        relation="rel_company_id_valid",
        column1="company_id",
        column2="group_id",
    )
    product_category_restart_grp_ids = fields.Many2many(
        string="Allow To Restart Category",
        comodel_name="res.groups",
        relation="rel_company_id_restart",
        column1="company_id",
        column2="group_id",
    )
