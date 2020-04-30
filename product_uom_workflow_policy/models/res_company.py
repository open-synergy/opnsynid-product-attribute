# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResCompany(models.Model):
    _name = "res.company"
    _inherit = "res.company"

    product_uom_confirm_grp_ids = fields.Many2many(
        string="Allow To Confirm Uom",
        comodel_name="res.groups",
        relation="rel_company_id_confirm_uom",
        column1="company_id",
        column2="group_id",
    )
    product_uom_valid_grp_ids = fields.Many2many(
        string="Allow To Validate Uom",
        comodel_name="res.groups",
        relation="rel_company_id_valid_uom",
        column1="company_id",
        column2="group_id",
    )
    product_uom_restart_grp_ids = fields.Many2many(
        string="Allow To Restart Uom",
        comodel_name="res.groups",
        relation="rel_company_id_restart_uom",
        column1="company_id",
        column2="group_id",
    )
