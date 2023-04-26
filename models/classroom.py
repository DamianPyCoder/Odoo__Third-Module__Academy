# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClassRoom(models.Model):
    _name = 'openacademy.classroom'

    name = fields.Char(string='Title', required=True)
    number_of_seats = fields.Integer(string="Number of seats")
    has_screen = fields.Boolean(default=False)
    screen_size = fields.Selection([('big', '88IN'), ('medium', '75IN'), ('small', '65IN')])

    @api.onchange('has_screen')
    def _onchange_has_screen(self):
        if self.has_screen:
            self.screen_size = 'medium'
        else:
            self.screen_size = None