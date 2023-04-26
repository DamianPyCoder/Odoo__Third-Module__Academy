# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(string="Title", required=True)
    start_date = fields.Date(string="Start date")
    classroom_id = fields.Many2one('openacademy.classroom')

    instructor_id = fields.Many2one('res.partner')
    course_id = fields.Many2one('openacademy.course')
    attendee_ids = fields.Many2many('res.partner')

    number_of_seats = fields.Integer(compute="_compute_number_of_seats")
    taken_seats = fields.Integer(compute='_compute_taken_seats')

    @api.depends('classroom_id')
    def _compute_number_of_seats(self):
        for record in self:
            if self.classroom_id:
                self.number_of_seats = self.classroom_id.number_of_seats
            else:
                self.number_of_seats = 0

    @api.depends('number_of_seats','attendee_ids')
    def _compute_taken_seats(self):
        for record in self:
            if self.number_of_seats and self.number_of_seats > 0:
                self.taken_seats = len(self.attendee_ids)*100/self.number_of_seats
            else:
                self.taken_seats = 0

