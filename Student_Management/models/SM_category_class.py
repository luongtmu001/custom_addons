from odoo import fields, models, api


class SMClass(models.Model):
    _name = "sm.class"
    _description = "Danh mục lớp học"
    _inherit = "sm.category"  # _inherits là đa kế thừa, _inherit là đơn kế thừa

    schoolyear_id = fields.Many2one('sm.schoolyear', string="Niên khóa")
    major_id = fields.Many2one('sm.student.major', string="Ngành học")

