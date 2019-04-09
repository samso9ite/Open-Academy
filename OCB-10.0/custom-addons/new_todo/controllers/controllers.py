# -*- coding: utf-8 -*-
from odoo import http

# class NewTodo(http.Controller):
#     @http.route('/new_todo/new_todo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_todo/new_todo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_todo.listing', {
#             'root': '/new_todo/new_todo',
#             'objects': http.request.env['new_todo.new_todo'].search([]),
#         })

#     @http.route('/new_todo/new_todo/objects/<model("new_todo.new_todo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_todo.object', {
#             'object': obj
#         })