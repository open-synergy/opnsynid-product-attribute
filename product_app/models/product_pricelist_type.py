# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProductPricelistType(models.Model):
    _inherit = "product.pricelist.type"

    menu_id = fields.Many2one(
        string="Menu",
        comodel_name="ir.ui.menu",
        readonly=True,
    )
    waction_id = fields.Many2one(
        string="Window Action",
        comodel_name="ir.actions.act_window",
        readonly=True,
    )

    @api.multi
    def action_create_menu(self):
        for price in self:
            waction = self._create_waction()
            menu = self._create_menu(waction)
            price.write({
                "waction_id": waction.id,
                "menu_id": menu.id,
            })

    @api.multi
    def action_remove_menu(self):
        for price in self:
            price._unlink_waction_menu()

    @api.multi
    def _create_waction(self):
        self.ensure_one()
        obj_waction = self.env["ir.actions.act_window"]
        return obj_waction.create(
            self._prepare_waction_data())

    @api.multi
    def _prepare_waction_data(self):
        self.ensure_one()
        return {
            "name": self.name,
            "type": "ir.actions.act_window",
            "res_model": "product.pricelist",
            "view_mode": "tree,form",
            "view_type": "form",
            "domain": [("type", "=", self.key)],
            "context": {"default_type": self.key, 'type_invisible': True},
        }

    @api.multi
    def _create_menu(self, waction):
        self.ensure_one()
        obj_menu = self.env["ir.ui.menu"]
        return obj_menu.create(
            self._prepare_menu_data(waction))

    @api.multi
    def _prepare_menu_data(self, waction):
        self.ensure_one()
        return {
            "name": self.name,
            "sequence": 100,
            "parent_id": self.env.ref(
                "product_app.product_pricelist_menu").id,
            "action": "ir.actions.act_window, %s" % (waction.id),
        }

    @api.multi
    def _unlink_waction_menu(self):
        self.ensure_one()
        self.menu_id.unlink()
        self.waction_id.unlink()
