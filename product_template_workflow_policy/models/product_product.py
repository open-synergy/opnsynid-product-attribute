# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProductProduct(models.Model):
    # jika 1 inherit tdk perlu buat _name
    _name = "product.product"
    _inherit = [
        "product.product",
    ]

    active = fields.Boolean(
        default=False,
        readonly=True,
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
