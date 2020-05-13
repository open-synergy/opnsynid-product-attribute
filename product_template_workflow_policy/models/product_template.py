# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProductTemplate(models.Model):
    # jika 1 inherit tdk perlu buat _name
    _name = "product.template"
    _inherit = [
        "product.template",
        "base.workflow_policy_object",
    ]

    @api.depends(
        "company_id",
    )
    # membuat fungsi untuk field compute -->
    @api.multi
    def _compute_policy(self):
        _super = super(ProductTemplate, self)
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
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        compute="_compute_company_id",
        store=False,
        default=lambda self: self._get_company_id(),
    )
    name = fields.Char(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    sale_ok = fields.Boolean(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    type = fields.Selection(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    list_price = fields.Float(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    description = fields.Text(
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
    standard_price = fields.Float(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    seller_ids = fields.One2many(
        comodel_name="product.supplierinfo",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    description_purchase = fields.Text(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    product_manager = fields.Many2one(
        comodel_name="res.users",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    volume = fields.Float(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    weight = fields.Float(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    warranty = fields.Float(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    weight_net = fields.Float(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    description_sale = fields.Text(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    attribute_line_ids = fields.One2many(
        comodel_name="product.attribute.line",
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

    # fungsi saat menekan tombol confirm - valid restart dilakukan
    # perubahan data state user dan tanggal dengan menjalankan fungsi
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
        }
        return result
