# -*- coding: utf-8 -*-

from odoo import models, fields, api

class openacademy(models.Model):
    _name = 'openacademy.teachers'

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")

class Courses(models.Model):
    _inherit = 'product.template'

    name = fields.Char()
    teacher_id = fields.Many2one('openacademy.teachers', string="Teacher")
