# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product Halal",
    "version": "8.0.1.0.0",
    "summary": "Product's halal certificate information",
    "category": "Product",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "product",
        "product_certificate"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_view.xml"
    ],
}