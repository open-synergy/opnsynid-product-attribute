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
        self.obj_product = self.env['product.product']

        # Data UOM
        self.uom_unit = self.env.ref('product.product_uom_unit')

        # Data Product
        self.product_1 = self.create_product()
        self.product_2 = self.env.ref("product.product_product_2")
        self.product_3 = self.env.ref("product.product_product_3")

    def create_product(self):
        # Create product template
        template = self.obj_product_template.create({
            'name': 'Template Test',
            'uom_id': self.uom_unit.id,
        })
        # Create product
        product = self.obj_product.create({
            'name': 'Test Product 1',
            'standard_price': 1,
            'type': 'consu',
            'uom_id': self.uom_unit.id,
            'default_code': 'A',
            'product_tmpl_id': template.id,
        })

        return product

    def test_product_halal_status_1(self):
        # CONDITION
        # Using new product
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
        # Using existing product
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
        # Using existing product
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
