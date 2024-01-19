# -*- coding: utf-8 -*-
from odoo import http


class MyTorontoTax(http.Controller):
    @http.route('/my_toronto_tax/my_toronto_tax', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/my_toronto_tax/my_toronto_tax/objects', auth='public')
    def list(self, **kw):
        return http.request.render('my_toronto_tax.listing', {
            'root': '/my_toronto_tax/my_toronto_tax',
            'objects': http.request.env['my_toronto_tax.my_toronto_tax'].search([]),
        })

    @http.route('/my_toronto_tax/my_toronto_tax/objects/<model("my_toronto_tax.my_toronto_tax"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_toronto_tax.object', {
            'object': obj
        })
    
    @http.route('/my_toronto_tax/documents', auth='user')
    def upload_document(self, **kw):
        values = self._prepare_portal_layout_values()
        return http.request.render('portal.portal_my_home', values)