# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests import common
from datetime import datetime, date


class TestProductHalal(common.TransactionCase):

    def setUp(self):
        super(TestProductHalal, self).setUp()
        # Objects
        self.obj_product_template = self.env["product.template"]

        # Data Product
        self.product_1 = self.env.ref("product.product_product_1")
        self.product_2 = self.env.ref("product.product_product_2")
        self.product_3 = self.env.ref("product.product_product_3")

    def test_product_halal_status_1(self):
        # CONDITION
        # date_start = True
        # date_end = False

        self.product_1.halal_ids = [
            (0, 0, {
                'name': 'Certificate No.1',
                'date_start': '2016-01-01'})
        ]
        self.assertEqual(
            self.product_1.halal_state, "certified")

    def test_product_halal_status_2(self):
        # CONDITION
        # date_start = True
        # date_end < date.now

        date_now = datetime.now().strftime("%Y-%m-%d")

        date_end = date.fromordinal(
            datetime.strptime(
                date_now, '%Y-%m-%d').toordinal() - 10)

        self.product_2.halal_ids = [
            (0, 0, {
                'name': 'Certificate No.1',
                'date_start': '2016-01-01',
                'date_end': date_end})
        ]
        self.assertEqual(
            self.product_2.halal_state, "not_certified")

    def test_product_halal_status_3(self):
        # CONDITION
        # date_start = True
        # date_end > date.now

        date_now = datetime.now().strftime("%Y-%m-%d")

        date_end = date.fromordinal(
            datetime.strptime(
                date_now, '%Y-%m-%d').toordinal() + 10)

        self.product_3.halal_ids = [
            (0, 0, {
                'name': 'Certificate No.1',
                'date_start': '2016-01-01',
                'date_end': date_end})
        ]
        self.assertEqual(
            self.product_3.halal_state, "certified")
