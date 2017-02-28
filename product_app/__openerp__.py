# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product's Management Application",
    "version": "8.0.1.0.0",
    "summary": "Base module to manage product",
    "category": "Product Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "product",
    ],
    "data": [
        "security/res_groups.xml",
        "views/product_product_view.xml",
    ],
}
