from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import  re

STUDENT_CODE_REGEX = re.compile(r'^[A-Za-z0-9.]+$')

class studentManagementStudentList(models.Model):
    _name = "sm.student.list"
    _inherit = 'mail.thread'
    _description = "Quản lý sinh viên"

    code = fields.Char(size=64,string= "Mã sinh viên", required = True,tracking=True, compute='_check_student_code')
    name = fields.Char(string= "Tên sinh vên", required=True)
    address =  fields.Char(string= "Địa chỉ hiện tại", required=True)
    home_town =  fields.Char(string= "Quê quán", required=True)
    class_no = fields.Char(string="Lớp hành chính", required= True)
    birthday = fields.Date(string="Ngày sinh", required=True)
    id_card_no = fields.Char(string="Số CMND")
    id_card_date = fields.Date(string="Ngày cấp", required=True)
    id_card_place = fields.Char(string="Nơi cấp")
    phone = fields.Char(string="Số điện thoại")
    sex = fields.Selection([('male', 'Nam'),('female','Nữ'),('other', 'Khác')], string="Giới tính", help='Chọn giới tính', default="Chọn giới tính")
    image = fields.Binary(string="Ảnh", attachment=True)
    email = fields.Char(string="Email")

    @api.onchange('code')
    def _check_student_code(self):
        for student in self:
            if not re.match(STUDENT_CODE_REGEX, student.code):
                raise ValidationError(_(
                    "Mã sinh viên không được chứa ký tự đặc biệt."
                ))

    @api.depends('code') #viết hoa mã
    def _compute_capitalized_code(self):
        for rec in self:
            if rec.code:
                rec.code = rec.code.upper()
            else:
                rec.code = ''


