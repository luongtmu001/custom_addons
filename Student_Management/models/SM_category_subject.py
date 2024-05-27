from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class sm_category_class(models.Model):
    _name = "sm.category.subject"
    _description = 'Danh mục môn học'
    _inherit = 'sm.category'

    credits = fields.Float(string="Số tín chỉ", required=True, tracking=True)
    major_id = fields.Many2one('sm.student.major', string="Mã khoa")

    @api.constrains('credits')
    def _check_subject_credit(self):
        for cr in self:
            if (cr.credits <= 0):
                raise ValidationError(_(
                    "Số tín chỉ phải lớn hơn 0!"
                ))
