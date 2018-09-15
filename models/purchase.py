# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _
from odoo.exceptions import Warning

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def button_confirm(self):
        user_id = self.env['res.users'].search([('id', '=', self._uid)])
        account_id = False

        for line in self.order_line:
            if line.product_id.property_account_expense_id:
                account_id = line.product_id.property_account_expense_id
            elif line.product_id.property_account_income_id:
                account_id = line.product_id.property_account_income_id

            if account_id and account_id in [account_approve.account_id for account_approve in user_id.approver_ids]:
                for approve in user_id.approver_ids:
                    if approve.account_id == account_id:
                        if line.price_subtotal >= approve.minimum_allowed and line.price_subtotal <= approve.maximum_allowed:
                            continue
                        else:
                            self.write({
                                'state': 'to approve'
                            })
                            self.env.cr.commit()
                            raise Warning(_("Your don't the permission to sell the product %s for this price, please ask for approvance." % line.product_id.name))

            else:
                self.write({
                    'state': 'to approve'
                })
                self.env.cr.commit()
                if not account_id:
                    raise Warning(_(
                        "The product %s doesn't have an Expense Account. Please, register one." % line.product_id.name))
                elif account_id and account_id in [account_approve.account_id for account_approve in user_id.approver_ids]:
                    raise Warning(_(
                        "You don't have the necessary permission to sell the product %s. You'll need the approval to "
                        "confirm this Purchase Order") % line.product_id.name)

            res = super(PurchaseOrder, self).button_confirm()
            return res
