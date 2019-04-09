from odoo import models, fields, api


class TodoApp(models.Model):
     _name = 'todoapp'

     _description = 'This app enables user to enter their todo task and check if fulfilled'
     name = fields.Char('Description', required=True)
     is_done = fields.Boolean('Done?')
     active = fields.Boolean('Active?', default=True)

     @api.multi
     def toggle_is_done(self):
         for task in self:
             task.is_done = not task.is_done
             return True

     @api.model
     def clear_is_done(self):
         active_task = self.search([('is_done','=', True)])
         active_task.write({'active':False})
         return True

     #Iterating method
     # @api.model
     # def toggle_is_done(self):
     #     get_active_task = self.search([('is_done', '=', True)])
     #     for active_task in get_active_task:
     #        active_task.write({'active':False})
     #        return True


