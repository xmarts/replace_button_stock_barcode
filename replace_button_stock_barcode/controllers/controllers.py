# -*- coding: utf-8 -*-
from odoo import http

# class Test12(http.Controller):
#     @http.route('/test12/test12/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test12/test12/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test12.listing', {
#             'root': '/test12/test12',
#             'objects': http.request.env['test12.test12'].search([]),
#         })

#     @http.route('/test12/test12/objects/<model("test12.test12"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test12.object', {
#             'object': obj
#         })