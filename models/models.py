# -*- coding: utf-8 -*-

from odoo import models, fields, api

class openacademy(models.Model):
    _name = 'openacademy.teachers'

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('openacademy.courses', 'teacher_id', string="Courses")

class Courses(models.Model):
    _name = 'openacademy.courses'
    _inherit = 'mail.thread'

    name = fields.Char()
    teacher_id = fields.Many2one('openacademy.teachers', string="Teacher")
