# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product EC Number Information",
    "version": "8.0.1.0.0",
    "category": "Product",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "product",
    ],
    "data": [
        "security/ir.model.access.csv",
        "menu.xml",
        "views/product_ec_number_views.xml",
        "views/product_ec_number_category_views.xml",
        "views/product_template_views.xml",
        "views/product_product_views.xml"
    ],
}
