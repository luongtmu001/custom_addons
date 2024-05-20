from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import re

SCHOOL_YEAR_CODE_REGEX = re.compile(r'^[A-Za-z0-9.]+$')

class studentManagementSchoolYear(models.Model):
    _name = "sm.schoolyear"
    _inherit = 'mail.thread'
    _description = "Danh sách khóa học"

    code = fields.Char(size=64,string= "Mã khóa học", required = True,tracking=True, compute='_check_schoolyear_code')
    name = fields.Char(string= "Tên khóa học", required=True)
    start_year = fields.Date(string="Thời gian bắt đầu", required=True)
    end_year = fields.Date(string="Thời gian bắt đầu", required=True)

    @api.depends('code')
    def _check_schoolyear_code(self):
        for sy in self:
            if not re.match(SCHOOL_YEAR_CODE_REGEX, sy.code):
                raise ValidationError(_(
                    "Mã năm học không được chứa ký tự đặc biệt."
                ))
    
    @api.constrains('end_year')
    def _check_end_year(self):
        for ey in self:
            if (ey.end_year < ey.start_year):
                raise ValidationError(_(
                    "Thời gian kết thúc phải lớn hơn thời gian bắt đầu"
                ))

   