# -*- code:UTF-8 -*-
from odoo.tests.common import TransactionCase

class TestTodo(TransactionCase):
    def create_test(self):
        "Create a Todo"
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)
        #Text toggle Done
        task.toggle_is_done()
        self.assertTrue(task.is_done)
        # Text Clear_Is_done
        task.clear_is_done()
        self.assertFalse(task.active)

    def setUp(self,*args,**kwargs):
        result = super(TestTodo,self).setUp(*args, **kwargs)
        user_demo = self.env.ref('base.user_demo')
        self.env = self.env(user = user_demo)
        return result