from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import re

class studentManagementDept(models.Model): 
    _name = "sm.student.dept"
    _inherit = 'sm.category' # _inherits là đa kế thừa, _inherit là đơn kế thừa
    _description = "Khoa"

    FoundedYear = fields.Integer(string="Thời năm thành lập", required=True)



   