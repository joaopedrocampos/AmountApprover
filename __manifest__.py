# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Amount Approver',
    'summary': "Approver for supplier and customer invoices",
    'description': """Approver module
        * This module checks if the user has permission according to the rules defined on it.
		
		DEPENDE OF THE BRAZILIAN LOCALIZATION MADE BY TRUSTCODE
    """,
    'version': '1.0.0',
    'category': 'account',
    'author': 'João Pedro Campos',
    'license': 'AGPL-3',
    'website': 'https://github.com/joaopedro-campos',
    'depends': [
        'br_account',
        'sales_team',
        'purchase',
        'sale'
    ],
    'data': [
        'views/res_users_view.xml',
        'views/sale_order_views.xml',
        'security/approver_security.xml',
    ],
    'auto_install': False,
    'application': True,
}