from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import re

class studentManagementChuongTrinh(models.Model): 
    _name = "sm.student.chuongtrinh"
    _inherit = 'sm.category' # _inherits là đa kế thừa, _inherit là đơn kế thừa
    _description = "Chương trình đào tạo"



   