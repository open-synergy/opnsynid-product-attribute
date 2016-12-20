# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests import common
from datetime import datetime, date
from openerp.exceptions import Warning as UserError


class TestProductCertificate(common.TransactionCase):

    def setUp(self):
        super(TestProductCertificate, self).setUp()
        # Objects
        self.obj_product_certificate = self.env["product.certificate"]

    def test_constrains_date(self):
        # CONDITION
        # date_end < date_start
        new = self.obj_product_certificate.new()
        new.name = 'Certificate No.1'
        date_start = datetime.now().strftime("%Y-%m-%d")
        new.date_start = date_start
        date_end = date.fromordinal(
            datetime.strptime(
                date_start, '%Y-%m-%d').toordinal() - 10)
        new.date_end = date_end

        # Check Constrains
        self.assertRaises(
            UserError,
            lambda: new._check_date()
        )
