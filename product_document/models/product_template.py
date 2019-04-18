# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import models, fields, api, _
from openerp.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    document_ids = fields.One2many(
        comodel_name="product.document",
        inverse_name="product_tmpl_id",
        string="Document(s)",
    )

    @api.multi
    def _prepare_search_document_criteria(
            self, category_code, operator, value):
        self.ensure_one()
        result = [
            ("name", operator, value),
            ("category_id.code", "=", category_code),
            ("state", "=", "open"),
        ]
        return result

    @api.multi
    def _prepare_inverse_document_categ_criteria(
            self, category_code):
        self.ensure_one()
        result = [
            ("code", "=", category_code)
        ]
        return result

    @api.multi
    def _create_inverse_document_categ(self, category_code):
        self.ensure_one()
        obj_doc_categ =\
            self.env["product.document.category"]
        return obj_doc_categ.create(
            self._prepare_create_inverse_document_categ(category_code)
        )

    @api.multi
    def _prepare_create_inverse_document_categ(self, category_code):
        self.ensure_one()
        return {
            "code": category_code,
            "name": category_code,
        }

    @api.multi
    def _create_inverse_document(
            self, record, category, name):
        self.ensure_one()
        obj_doc =\
            self.env["product.document"]
        return obj_doc.create(
            self._prepare_create_inverse_document(record, category, name)
        )

    @api.multi
    def _prepare_create_inverse_document(
            self, record, category, name):
        self.ensure_one()
        return {
            "product_tmpl_id": record.id,
            "category_id": category.id,
            "name": name,
        }

    @api.multi
    @api.depends("document_ids")
    def _compute_document(self, field_name, category_code):
        for record in self:
            document_ids = record.document_ids.filtered(
                lambda r: r.category_id.code == category_code
            )
            if not document_ids:
                continue
            value = document_ids[0].name
            record[field_name] = value

    @api.multi
    def _inverse_document(self, field_name, category_code):
        obj_doc_categ =\
            self.env["product.document.category"]
        for record in self:
            document_id = record.document_ids.filtered(
                lambda r: r.category_id.code == category_code
            )
            record_len = len(document_id)
            if record_len == 0:
                name = record[field_name]
                if not name:
                    continue
                criteria =\
                    self._prepare_inverse_document_categ_criteria(
                        category_code)
                category = obj_doc_categ.search(criteria)
                if not category:
                    category =\
                        self._create_inverse_document_categ(
                            category_code)
                self._create_inverse_document(
                    record, category, name
                )
            elif record_len == 1:
                value = record[field_name]
                if value:
                    document_id.name = value
                else:
                    document_id.active = False
            else:
                raise ValidationError(_(
                    "This %s has multiple Documents of this type (%s),"
                    "so a write via the %s field is not possible."
                    "In order to fix this,"
                    "please use the Documents tab.",
                ) % (
                    record._name, category_code, field_name,
                ))

    @api.model
    def _search_document(self, category_code, operator, value):
        obj_prod_doc =\
            self.env["product.document"]
        criteria = self._prepare_search_document_criteria(
            category_code, operator, value)
        document_ids = obj_prod_doc.search(criteria)
        return [
            ("document_ids.id", "in", document_ids.ids),
        ]
