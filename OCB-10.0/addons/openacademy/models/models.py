# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import timedelta
class Course(models.Model):
    _name = "openacademy.course"
    name  =  fields.Char(string="Title", required="True")
    description = fields.Char()

    responsible_id = fields.Many2one('res.users',ondelete='set null',string="Responsible",index=True)
    session_id = fields.One2many('session', "course_id", string="Sessions")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         'Name must not be the same as description'
         ),

        ('name_unique',
         'UNIQUE(name)',
         'error: The course title must be unique'
         ),
    ]

    # Adding a constraint to prevent duplication of names
    # @api.constrains('name')
    # def prevent_duplication_of_name(self):
    #     rec_to_search = self.env['Course']
    #     for rec in self:
    #         search_rec = rec_to_search.search([('name','=like','name')])
    #         if search_rec:
    #             raise exceptions.ValidationError("A course with the same name already exist in the database")
    @api.multi
    def copy(self, default=None):
        default=(default or {})

        copied_count = self.search_count([('name','=like',u'Copy of {}%'.format(self.name))])
        if copied_count:
            return {
                'warning':{
                    'Title': "Name already exist",
                    'message': "Name already exist in the database"
            },
            }
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {}({})".format(self.name,copied_count)
        default['name'] = new_name
        return super(Course,self).copy(default)



class Session(models.Model):
    _name = "session"
    name = fields.Char(required="True")
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(string="Activate Session",default=True)
    color = fields.Integer()

    instructor_id = fields.Many2one('res.partner',string="Instructor",
                                    domain=[('employee','=',True)],store=True)
    course_id = fields.Many2one("openacademy.course", ondelete="cascade",string="Course",required=True)
    attendee_id = fields.Many2many("res.partner", string="Attendees")
    end_date = fields.Date(string="End Date",compute="_get_session_end_date",inverse="_set_session_end_date",store=True)
    hours = fields.Float(string='Hours to use', compute='_get_hours',inverse='_set_hours')
    attendee_count = fields.Integer(string='Number of attendees', store=True)
    taken_seats = fields.Float(string="Taken Seats",compute='taken_seats_model')
    state = fields.Selection([('draft', "Draft"), ('confirmed', "Confirmed"), ('done', "Done")])

    @api.multi
    def action_draft(self):
        self.state='draft'

    @api.multi
    def action_confirm(self):
        self.state='confirmed'

    @api.multi
    def action_done(self):
        self.state='done'

    @api.depends('start_date', 'duration')
    def _get_session_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            start_date = fields.Datetime.from_string(r.start_date)
            duration = timedelta(days=r.duration,seconds=-1)
            r.end_date = start_date + duration

    # @api.onchange('seats')
    # def num_of_attendees(self):
    #     num_of_seat = 0
    #     for r in self:
    #         num_of_seat= r.seats
    #     if num_of_seat < r.attendee_count:
    #

    def _set_session_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date).days + 1

    @api.depends('duration','start_date')
    def _get_hours(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.duration= 0.00
                continue
            r.hours = r.duration * 24

    def _set_hours(self):
        for r in self:
            r.duration = r.hours/24


    @api.onchange('attendee_count)')
    def taken_seats_model(self):
        for r in self:
            if not r.seats:
                r.taken_seats = "0.1"
            else:
                r.taken_seats = 100 * r.attendee_count/r.seats

    @api.onchange('seats','attendee_count')
    def invalid_input(self):
        if self.seats < 0:
            return {
                'warning':{
                    'title': "Incorrect seat value",
                    'message': "Please input a valid seat number"
                },
            }
        else:
            if self.seats < self.attendee_count:
                return {
                    'warning':{
                        'title': "Attendees are more than seat",
                        'message': "Attenders are more than the available seats, Let them wait for the next batch"
                    },
                }
    @api.constrains('instructor_id', 'attendee_id')
    def _check_if_instructor_is_present(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_id:
                raise exceptions.ValidationError("A session instructor can't be an instructor")