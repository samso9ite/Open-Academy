# -*- coding: utf-8 -*-
from odoo import http

# class NewestTodo(http.Controller):
#     @http.route('/newest_todo/newest_todo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/newest_todo/newest_todo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('newest_todo.listing', {
#             'root': '/newest_todo/newest_todo',
#             'objects': http.request.env['newest_todo.newest_todo'].search([]),
#         })

#     @http.route('/newest_todo/newest_todo/objects/<model("newest_todo.newest_todo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('newest_todo.object', {
#             'object': obj
#         })