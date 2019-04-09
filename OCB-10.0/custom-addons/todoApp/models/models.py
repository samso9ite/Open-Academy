# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class todoApp(models.Model):
#     _name = 'todoApp.todoApp'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
# -*- coding: utf-8 -*-
# from odoo import models, fields
#
#
# class TodoApp(models.Model):
#      _name = 'todoapp'
#
#      _description = 'This app enables user to enter their todo task and check if fulfulled'
#      name = fields.Char('Description', required=True)
#      is_done = fields.Boolean('Done?')
#      active = fields.Boolean('Active?', default=True)
# from . import todo_model
