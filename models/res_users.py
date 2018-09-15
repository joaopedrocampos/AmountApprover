# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _

class ResUsers(models.Model):
    _inherit = 'res.users'

    approver_ids = fields.One2many('amount.approver.line', 'user_id')