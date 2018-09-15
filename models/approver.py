# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AmountApprover(models.Model):
    _name = 'amount.approver'

class AmountApproverLine(models.Model):
    _name = 'amount.approver.line'

    user_id = fields.Many2one('res.users', "User")
    account_id = fields.Many2one('account.account', "Account")
    minimum_allowed = fields.Float("Minimum Allowed")
    maximum_allowed = fields.Float("Maximum Allowed")