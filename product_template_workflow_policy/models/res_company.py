# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResCompany(models.Model):
    _name = "res.company"
    _inherit = "res.company"

    product_template_confirm_grp_ids = fields.Many2many(
        string="Allow To Confirm Product Template",
        comodel_name="res.groups",
        relation="rel_company_id_confirm_product_template",
        column1="company_id",
        column2="group_id",
    )
    product_template_valid_grp_ids = fields.Many2many(
        string="Allow To Validate Product Template",
        comodel_name="res.groups",
        relation="rel_company_id_valid_product_template",
        column1="company_id",
        column2="group_id",
    )
    product_template_restart_grp_ids = fields.Many2many(
        string="Allow To Restart Product Template",
        comodel_name="res.groups",
        relation="rel_company_id_restart_product_template",
        column1="company_id",
        column2="group_id",
    )
