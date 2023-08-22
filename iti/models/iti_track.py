# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
class ItiTrack(models.Model):
     _name = "iti.track"
     # _rec_name ="capacity"


     name = fields.Char(string="Name")
     is_open = fields.Boolean()
     capacity = fields.Integer()


     student_ids = fields.One2many("iti.student" , "track_id")




