# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
class ItiSkill(models.Model):
     _name = "iti.skill"

     name = fields.Char(string="Name")
