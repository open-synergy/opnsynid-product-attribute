# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp
from openerp.tools.translate import _


class AddToPricelistItem(models.AbstractModel):
    _name = "product.add_to_pricelist_item"
    _description = "Abstract Module to Add Pricelist Item"

    @api.model
    def _price_field_get(self):
        pt = self.env["product.price.type"]
        result = []
        for line in pt.search([]):
            result.append((line.id, line.name))

        result.append((-1, _("Other Pricelist")))
        result.append((-2, _("Supplier Prices on the product form")))
        return result

    min_quantity = fields.Integer(
        string="Min. Quantity",
        required=True,
        help="For the rule to apply, bought/sold quantity must be greater "
        "than or equal to the minimum quantity specified in this field.\n"
        "Expressed in the default UoM of the product."
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        help="Gives the order in which the pricelist items will be checked. "
             "The evaluation gives highest priority to lowest sequence and "
             "stops as soon as a matching item is found.",
    )
    base = fields.Selection(
        selection=_price_field_get,
        string="Based on",
        required=True,
        size=-1,
        help="Base price for computation.",
    )
    base_pricelist_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Other Pricelist",
    )
    price_surcharge = fields.Float(
        string="Price Surcharge",
        digits_compute=dp.get_precision("Product Price"),
        help="Specify the fixed amount to add or substract(if negative) "
             "to the amount calculated with the discount.",
    )
    price_discount = fields.Float(
        string="Price Discount",
        digits=(16, 4),
    )
    price_round = fields.Float(
        string="Price Rounding",
        digits_compute=dp.get_precision("Product Price"),
        help="Sets the price so that it is a multiple of this value.\n"
        "Rounding is applied after the discount and before the surcharge.\n"
        "To have prices that end in 9.99, set rounding 10, surcharge -0.01",
    )
    price_min_margin = fields.Float(
        string="Min. Price Margin",
        digits_compute=dp.get_precision("Product Price"),
        help="Specify the minimum amount of margin over the base price.",
    )
    price_max_margin = fields.Float(
        string="Max. Price Margin",
        digits_compute=dp.get_precision("Product Price"),
        help="Specify the maximum amount of margin over the base price.",
    )

    @api.multi
    def button_apply(self):
        self.ensure_one()
        self._create_pricelist_items()

    @api.multi
    def _prepare_pricelist_item_data(self):
        self.ensure_one()
        result = {
            "price_version_id": self._context.get("active_id", False),
            "min_quantity": self.min_quantity,
            "sequence": self.sequence,
            "base": self.base,
            "base_pricelist_id": self.base_pricelist_id and
            self.base_pricelist_id.id or False,
            "price_surcharge": self.price_surcharge,
            "price_discount": self.price_discount,
            "price_round": self.price_round,
            "price_min_margin": self.price_min_margin,
            "price_max_margin": self.price_max_margin,
        }
        return result

    @api.multi
    def _create_pricelist_items(self):
        pass
