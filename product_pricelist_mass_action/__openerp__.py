# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product Pricelist Mass Action",
    "version": "8.0.1.2.0",
    "category": "Product",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "product",
    ],
    "data": [
        "wizards/add_to_pricelist_item.xml",
        "wizards/add_product_to_pricelist_item.xml",
        "wizards/add_product_template_to_pricelist_item.xml",
        "wizards/add_product_category_to_pricelist_item.xml",
        "views/product_pricelist_version_views.xml",
    ],
}
