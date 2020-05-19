# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _name = "product.product"
    _inherit = [
        "product.product",
        "base.workflow_policy_object",
    ]

    @api.depends(
        "company_id",
    )
    @api.multi
    def _compute_policy(self):
        _super = super(ProductProduct, self)
        _super._compute_policy()

    @api.multi
    def _compute_company_id(self):
        for document in self:
            document.company_id = self.env.user.company_id

    @api.multi
    def _get_company_id(self):
        return self.env.user.company_id

    active = fields.Boolean(
        default=False,
        readonly=True,
    )
    product_active = fields.Boolean(
        default=False,
        readonly=True,
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        compute="_compute_company_id",
        store=False,
        default=lambda self: self._get_company_id(),
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting For Approval"),
            ("valid", "Valid"),
        ],
        default="draft",
        required=True,
    )
    lst_price = fields.Float(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    ean13 = fields.Char(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    default_code = fields.Char(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    # Policy Fields
    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy"
    )
    valid_ok = fields.Boolean(
        string="Can Valid",
        compute="_compute_policy"
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy"
    )
    # Log Fields
    confirm_date = fields.Datetime(
        string="Confirm Date",
        readonly=True,
    )
    confirm_user_id = fields.Many2one(
        string="Confirmed By",
        comodel_name="res.users",
        readonly=True,
    )
    valid_date = fields.Datetime(
        string="Valid Date",
        readonly=True,
    )
    valid_user_id = fields.Many2one(
        string="Valid By",
        comodel_name="res.users",
        readonly=True,
    )
    restart_date = fields.Datetime(
        string="Restart Date",
        readonly=True,
    )
    restart_user_id = fields.Many2one(
        string="Restart By",
        comodel_name="res.users",
        readonly=True,
    )

    @api.multi
    def write(self, vals):
        for document in self:
            _logger.info("vals: %s", vals)
            _logger.info("product_active: %s", document.product_active)
            if "active" in vals and "product_active" not in vals:
                vals["active"] = document.product_active
            super(ProductProduct, document).write(vals)
        return True

    @api.multi
    def action_confirm(self):
        for document in self:
            document.write(document._prepare_confirm_data())

    @api.multi
    def action_valid(self):
        for document in self:
            document.write(document._prepare_valid_data())

    @api.multi
    def action_restart(self):
        for document in self:
            document.write(document._prepare_restart_data())

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        result = {
            "state": "confirm",
            "confirm_date": fields.Datetime.now(),
            "confirm_user_id": self.env.user.id,
            "restart_date": False,
            "restart_user_id": False,
        }
        return result

    @api.multi
    def _prepare_valid_data(self):
        self.ensure_one()
        result = {
            "state": "valid",
            "valid_date": fields.Datetime.now(),
            "valid_user_id": self.env.user.id,
            "active": True,
            "product_active": True,
        }
        return result

    @api.multi
    def _prepare_restart_data(self):
        self.ensure_one()
        result = {
            "state": "draft",
            "restart_date": fields.Datetime.now(),
            "restart_user_id": self.env.user.id,
            "confirm_date": False,
            "confirm_user_id": False,
            "valid_date": False,
            "valid_user_id": False,
            "active": False,
            "product_active": False,
        }
        return result
