from odoo import models,fields
class Todo_task(models.Model):
    _name = 'todolist'
    _description = 'Todo_Task'
    name = fields.Char('Description', required= True)
    is_done = fields.Boolean('Done ?')
    active = fields.Boolean('Active ?', default = True)