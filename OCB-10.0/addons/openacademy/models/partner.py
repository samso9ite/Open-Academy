from odoo import models, fields
class partners(models.Model):
    _inherit = 'res.partner'
    # Adding a new field to the partner module(session)
    employee = fields.Boolean("Instructor", default=False)
    session_id = fields.Many2many('session', string="Attended Sessions", readonly=True)
