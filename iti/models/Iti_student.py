# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class Iti_student(models.Model):
     _name = "iti.student"
     name = fields.Char(string="Name")
     email = fields.Char()
     birth_date = fields.Date()
     salary = fields.Float()
     tax = fields.Float(compute ="calc_tax" , store=True)

     address = fields.Text()
     gender = fields.Selection([('m', "Male"), ('f', "Female")], default="m")
     accepted = fields.Boolean()
     level = fields.Integer()
     image = fields.Binary()
     cv = fields.Html()
     interview_time = fields.Datetime()

     track_id = fields.Many2one("iti.track")


     skill_id = fields.Many2many("iti.skill")

     grade_ids = fields.Many2one("student.course.line","student_id")

     track_capasity = fields.Integer(related="track_id.capacity")

     state = fields.Selection([
          ('applied', "Applied"),
          ('first', "First interview"),
          ('second', "Second iNTERVIW"),
          ('passed', "Passed"),
          ('rejected', "Rejected"),
     ],default="applied")

     # @api.multi
     @api.depends('salary')
     def calc_tax(self):
          for student in self:
               student.tax = student.salary*0.20



     _sql_constraints = [
          ('unique_name', 'UNIQUE(name)', 'This name already exists.'),
     ]


     # ..............................
     @api.model
     def create(self, vals):

          new_student = super().create(vals)
          name_split = new_student.name.split()
          new_student.email = f"{name_split[0][0]}{name_split[1]} @ gmail.com"
          return new_student


     # @api.multi
     def write(self,vals):

          if "name" in vals:
               name_split = vals['name'].split()
               vals['email'] = f"{name_split[0][0]}{name_split[1]} @ gmail.com"

          super().write(vals)
# ..............................
#      @api.multi
     def unlink(self):
          for record in self:
               if record.state  in ['passed', 'rejected']:
                    raise UserError("you cant delet passed/rejected row ")
          super().unlink()


     @api.constrains("salary")
     def check_salary(self):
          if self.salary>10000:
               raise UserError("salary cant be greater than 10000")

# ..............................

     def change_state(self):
          if self.state =='applied':
               self.state='first'
          elif self.state == 'first':
               self.state='second'
          elif self.state in ['passed','rejected']:
               self.state='applied'

     def set_passed(self):
          self.state ="passed"

     def set_rejected(self):
          self.state ="rejected"





     def set_first(self):

          self.state='first'
          self.salary=3000






















     @api.onchange("gender")
     def _on_change_gender(self):
          domain = {'track_id':[]}

          if self.gender == 'm':
               domain = {'track_id': [('is_open', '=', True)]}

               self.salary =10000
          else:
               self.salary =5000

          return {
               'warning':{
                    'title':'you change gander value',
                    'message':'change gender and salary value'
               },
               'domain':domain

}






















class ItiCourse(models.Model):
     _name = "iti.course"

     name = fields.Char(string="Name")







class StudentGrade(models.Model):
     _name = "student.course.line"

     name = fields.Char(string="Name")

     student_id = fields.Many2one("iti.student")
     course_id = fields.Many2one("iti.course")
     grade = fields.Selection([('g', "Good"), ('vg', "very good"),])

