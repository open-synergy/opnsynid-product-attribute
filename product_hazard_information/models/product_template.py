# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductHazardStatement(models.Model):
    _name = "product.hazard_statement"
    _description = "Product Hazard Statement"

    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.template",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
    )
    hazard_statement_id = fields.Many2one(
        string="Hazard Statement",
        comodel_name="product.ghs_hazard_statement",
        required=True,
    )


class ProductHazardPrecautionaryStatement(models.Model):
    _name = "product.hazard_precautionary_statement"
    _description = "Product Hazard Precautionary Statement"

    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.template",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
    )
    hazard_precautionary_statement_id = fields.Many2one(
        string="Hazard Precautionary Statement",
        comodel_name="product.ghs_hazard_precautionary_statement",
        required=True,
    )


class ProductHazardPictogram(models.Model):
    _name = "product.hazard_pictogram"
    _description = "Product Hazard Pictogram"

    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.template",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
    )
    hazard_pictogram_id = fields.Many2one(
        string="Hazard Pictogram",
        comodel_name="product.ghs_hazard_pictogram",
        required=True,
    )
    image = fields.Binary(
        string="Pictogram",
        related="hazard_pictogram_id.image",
        store=False,
    )


class ProductTemplate(models.Model):
    _inherit = "product.template"

    hazard_statement_ids = fields.One2many(
        string="Hazard Statement",
        comodel_name="product.hazard_statement",
        inverse_name="product_id",
    )

    hazard_precautionary_statement_ids = fields.One2many(
        string="Hazard Precautionary Statement",
        comodel_name="product.hazard_precautionary_statement",
        inverse_name="product_id",
    )

    hazard_pictogram_ids = fields.One2many(
        string="Hazard Pictogram",
        comodel_name="product.hazard_pictogram",
        inverse_name="product_id",
    )
