from odoo.tests.common import TransactionCase
class Testing_new_todo(TransactionCase):
    #Creating a test enviroment
    def test_create(self):
        Todo = self.env['todolist']
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)
