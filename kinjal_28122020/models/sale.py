from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'sale.order'

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('approve', 'Waiting For Approval'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')


    def action_confirm(self):
        # flag = self.env.user.has_group('sales_team.group_sale_manager')
        res = super(SaleOrder,self).action_confirm()
        self.write({
            'state': 'approve',
        })
        return res

    def action_approve(self):
        res = super(SaleOrder,self).action_confirm()
        return res


    def action_reject(self):
        res = super(SaleOrder,self).action_cancel()
        return res
