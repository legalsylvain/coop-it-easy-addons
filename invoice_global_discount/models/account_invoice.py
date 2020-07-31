# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models

from odoo.addons import decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    global_discount = fields.Float(
        string="Global discount(%)",
        digits=dp.get_precision("Discount"),
        default=0.0,
    )

    @api.multi
    def propagate_discount_on_lines(self):
        self.ensure_one()
        for line in self.invoice_line_ids:
            line.discount = self.global_discount

        self.compute_taxes()
