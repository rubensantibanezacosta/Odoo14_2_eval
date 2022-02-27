# -*- coding: utf-8 -*-
# from odoo import http


# class Incidencias(http.Controller):
#     @http.route('/incidencias/incidencias/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/incidencias/incidencias/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('incidencias.listing', {
#             'root': '/incidencias/incidencias',
#             'objects': http.request.env['incidencias.incidencias'].search([]),
#         })

#     @http.route('/incidencias/incidencias/objects/<model("incidencias.incidencias"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('incidencias.object', {
#             'object': obj
#         })
