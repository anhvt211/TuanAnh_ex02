from odoo import models, fields

class EmployeeCertification(models.Model):
    _name = 'employee.certification'
    _description = 'Employee Certification'

    name = fields.Char(string="Certification Name", required=True)
    years = fields.Integer(string="Years Gained", required=True)
    employee_ids = fields.Many2many('hr.employee', string="Employee", ondelete='cascade')
