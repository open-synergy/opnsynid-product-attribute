# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product's SNI Certificate Management",
    "version": "8.0.1.0.0",
    "summary": "Manage product's SNI certificate information",
    "category": "Product",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["product_certificate"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_kode_teknis_sni_view.xml",
        "views/product_ics_sni_view.xml",
        "views/product_standar_sni_view.xml",
        "views/product_template_view.xml",
        "views/product_sni_menu.xml"
    ],
}
