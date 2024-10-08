from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError


class Employee_Plus(models.Model):
    _inherit = 'hr.employee'

    years_of_experience = fields.Integer(string="Years of Experience", default=0)
    is_years_of_experience = fields.Boolean(compute='set_is_years_of_experience')
    certification_ids = fields.Many2many('employee.certification', string="Certifications")
    skills_ids = fields.Many2many('employee.skills', string="Skills")

    has_certifications = fields.Boolean(string="Has Certifications", compute='_compute_has_certifications', store=True)

    @api.constrains('years_of_experience')
    def _check_years_of_experience(self):
        for rec in self:
            if  rec.years_of_experience > 30 or rec.years_of_experience < 0:
                raise ValidationError("Years of experience cannot exceed <0 and >30 years.")

    def set_is_years_of_experience(self):
        self.is_years_of_experience = self.env.user.has_group('employee_plus.group_hr_employee_experience_manager')

    # @api.model
    # def fields_get(self, allfields=None, attributes=None):
    #     res = super(Employee_Plus, self).fields_get(allfields, attributes=attributes)
    #     if 'years_of_experience' in res:
    #         if not self.env.user.has_group('employee_plus.group_hr_employee_experience_manager') :
    #             res['years_of_experience']['readonly'] = True
    #     return res

    def action_do_something(self):
        if not self.env.user.has_group('employee_plus.group_hr_employee_experience_manager'):
            raise UserError(_("You do not have access"))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Update Years of Experience',
            'res_model': 'employee.mass.update.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('employee_plus.view_employee_mass_update_wizard_form').id,
            'context': {
                # 'default_active_ids': self.id,
                'default_years_of_experience': self.years_of_experience,
                # 'default_message': 'Update this record?',
            },
            'target': 'new',
        }

    @api.depends('certification_ids')
    def _compute_has_certifications(self):
        for employee in self:
            # Kiểm tra xem có chứng chỉ nào không
            employee.has_certifications = bool(employee.certification_ids)

