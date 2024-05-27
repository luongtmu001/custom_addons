from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class sm_category_lecture(models.Model):
    _name = "sm.category.lecture"
    _description = 'Danh mục giảng khoa'
    _inherit = 'mail.thread'

    id_ct = fields.Many2one('sm.student.chuongtrinh', string="Mã chương trình", required=True, tracking =True)
    dept_id = fields.Many2one('sm.student.major', string="Mã khoa", required=True, tracking =True)
    subject_id = fields.Many2one('sm.category.subject', string="Mã môn học", required=True, tracking =True)
    school_year = fields.Many2one('sm.schoolyear', string="Năm học", required=True)
    terms = fields.Selection([('1', ' Học kỳ 1'), ('2', 'Học kỳ 2'), ('3', 'Học lỳ 3')], string="Học kỳ", required=True)
    credits = fields.Float(string="Số tín chỉ", required=True, tracking=True)
    theory = fields.Float(string="Số tiết lý thuyết", required=True, tracking=True)
    practice = fields.Float(string="Số tiết thực hành", required=True, tracking=True)
    remark = fields.Char(string="Ghi chú")
    @api.constrains('credits')
    def _check_subject_credit(self):
        for cr in self:
            if (cr.credits <= 0):
                raise ValidationError(_(
                    "Số tín chỉ phải lớn hơn 0!"
                ))
            
    @api.constrains('id_ct','dept_id','subject_id')
    def _check_constraint_major_subject_ct(self):
        for _check in self:
            self.env.cr.execute("SELECT Code FROM sm_student_chuongtrinh WHERE id = %s",(self.id_ct,))
            id_ct = self.env.cr.fetchone()[0]
            self.env.cr.execute("SELECT Code FROM sm_student_subject WHERE id = %s",(self.subject_id,))
            subject_id = self.env.cr.fetchone()[0]
            self.env.cr.execute("SELECT Code FROM sm_student_dept WHERE id = %s",(self.dept_id,))
            dept_id = self.env.cr.fetchone()[0]

            if (_check == id_ct) and (_check == subject_id) and (_check == dept_id):
                 raise ValidationError(_(
                    "Giá trị không hợp lệ! /n Mã môn học và mã khoa trong 1 chương trình đào tạo là duy nhất!"
                ))