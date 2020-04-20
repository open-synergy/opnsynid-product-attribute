# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Product UoM Category Workflow Policy",
    "version": "8.0.1.0.0",
    "category": "Product",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "product",
        "base_workflow_policy",
    ],
    "data": [
        "views/product_uom_categ_view.xml",        
    ],
}
