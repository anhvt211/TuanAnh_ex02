from odoo import models, fields

class EmployeeSkills(models.Model):
    _name = 'employee.skills'
    _description = 'Employee Skills'

    name = fields.Char(string="Skills Name", required=True)
    level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert')],
        string="Skill Level", default='beginner', required=True)
    employee_ids = fields.Many2many('hr.employee', string="Employee", ondelete='cascade')
