# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product Hazard Information",
    "version": "8.0.1.0.0",
    "category": "Product",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "product",
        "web_tree_image",
    ],
    "data": [
        "security/ir.model.access.csv",
        "menu.xml",
        "views/product_ghs_hazard_statement_views.xml",
        "views/product_ghs_hazard_precautionary_statement_views.xml",
        "views/product_ghs_hazard_pictogram_views.xml",
        "views/product_template_view.xml"
    ],
}
