from odoo import fields, models, api
from odoo.exceptions import UserError

class Employee_Mass_Update_Wizard(models.TransientModel):
    _name = "employee.mass.update.wizard"
    _description = 'Wizard to mass update employee skills, certifications, and experience'

    department_id=fields.Many2one('hr.department',string="Department")
    job_id=fields.Many2one('hr.job',string="Job Position")
    employee_ids=fields.Many2many('hr.employee', string="Employee",help="Select employees to update")
    skills_ids = fields.Many2many('employee.skills',string="Skills")
    certification_ids = fields.Many2many('employee.certification', string="Certifications")
    years_of_experience = fields.Integer(string="Years of Experience", default=0)

    @api.onchange('department_id', 'job_id')
    def _onchange_employee_filter(self):
        domain=[]
        if self.department_id:
            domain.append(('department_id', '=', self.department_id.id))
        if self.job_id:
            domain.append(('job_id', '=', self.job_id.id))
        employees = self.env['hr.employee'].search(domain)
        self.employee_ids = [(6, 0, employees.ids)]

    def action_update_employee_data(self):
        ids = self.env.context.get('active_ids')
        employees = self.env['hr.employee'].browse(ids)


        if self.years_of_experience < 5:
            raise UserError('Nhân viên này chưa có đủ 5 năm kinh nghiệm để được cập nhật.')
            # Thực hiện cập nhật dữ liệu nếu điều kiện thỏa mãn
        self.employee_id.write({
            'some_field': 'New Value'
        })
        return {'type': 'ir.actions.act_window_close'}

        for employee in employees:
            if self.years_of_experience:
                employee.write({'years_of_experience':self.years_of_experience})
            if self.skills_ids:
                employee.write({'skills_ids': [(4, skills.id) for skills in self.skills_ids]})
            if self.certification_ids:
                employee.write({'certification_ids': [(4, cert.id) for cert in self.certification_ids]})
    # def set_experience(self):
    #     ids = self.env.context.get('active_ids')
    #     employees = self.env['hr.employee'].browse(ids)
    #     for employee in employees:
    #         employee.years_of_experience = self.years_of_experience