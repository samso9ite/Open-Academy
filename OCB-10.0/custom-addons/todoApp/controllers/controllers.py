# -*- coding: utf-8 -*-
from odoo import http

# class Project2(http.Controller):
#     @http.route('/todoApp/todoApp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todoApp/todoApp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todoApp.listing', {
#             'root': '/todoApp/todoApp',
#             'objects': http.request.env['todoApp.todoApp'].search([]),
#         })

#     @http.route('/todoApp/todoApp/objects/<model("todoApp.todoApp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todoApp.object', {
#             'object': obj
#         })