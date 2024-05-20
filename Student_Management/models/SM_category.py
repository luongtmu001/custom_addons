from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import re

CATEGORY_CODE_REGEX = re.compile(r'^[A-Za-z0-9.]+$')

class SMcategory(models.Model):
    _name = 'sm.category'
    _inherit = 'mail.thread'
    _description = 'Cấu trúc chung danh mục'

    code = fields.Char(size=64,string= "Mã", required = True,tracking=True, compute='_check_category_code')
    name = fields.Char(string= "Tên", required=True)
    name2 = fields.Char(string= "Tên thứ 2", required=False)

    @api.constrains(code)
    def _check_category_code(self):
        for sy in self:
            if not re.match(CATEGORY_CODE_REGEX, sy.code):
                raise ValidationError(_(
                    "Mã không được chứa ký tự đặc biệt."
                ))
            
    @api.depends('code') #viết hoa mã
    def _compute_category_code(self):
        for rec in self:
            if rec.code:
                rec.code = rec.code.upper()
            else:
                rec.code = ''