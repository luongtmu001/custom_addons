from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import re


class studentManagementMajor(models.Model):
    _name = "sm.student.major"
    _inherit = 'sm.category'  # _inherits là đa kế thừa, _inherit là đơn kế thừa
    _description = "Ngành học"

    dept_id = fields.Many2one('sm.student.dept', string="Khoa")
