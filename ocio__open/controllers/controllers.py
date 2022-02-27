# -*- coding: utf-8 -*-
# from odoo import http


# class OcioOpen(http.Controller):
#     @http.route('/ocio__open/ocio__open/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ocio__open/ocio__open/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ocio__open.listing', {
#             'root': '/ocio__open/ocio__open',
#             'objects': http.request.env['ocio__open.ocio__open'].search([]),
#         })

#     @http.route('/ocio__open/ocio__open/objects/<model("ocio__open.ocio__open"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ocio__open.object', {
#             'object': obj
#         })
