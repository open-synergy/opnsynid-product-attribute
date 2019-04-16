# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product Document",
    "version": "8.0.1.0.0",
    "category": "Product Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "product"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_document_category_view.xml",
        "views/product_document_view.xml",
        "views/product_template_view.xml"
    ],
}
