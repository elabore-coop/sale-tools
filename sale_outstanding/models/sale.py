from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends("order_line.qty_delivered", "order_line.qty_invoiced", "order_line.qty_to_invoice", "order_line.price_unit")
    def _compute_sum_outstanding(self):
        for order in self:
            lines_outstanding = order.order_line.mapped(lambda r:(r.qty_to_invoice * r.price_unit))
            order["sum_outstanding"] = sum(lines_outstanding)

    @api.depends("order_line.qty_delivered", "order_line.product_uom_qty", "order_line.price_unit")
    def _compute_sum_pending_work(self):
        for order in self:
            lines_pending_work = order.order_line.mapped(lambda r:((r.product_uom_qty - r.qty_delivered) * r.price_unit) if not r.product_id or r.product_id.service_policy != 'ordered_timesheet' else 0)
            order["sum_pending_work"] = sum(lines_pending_work)


    sum_outstanding = fields.Monetary(_("Outstanding Untaxed"), readonly=True, store=True, compute="_compute_sum_outstanding")
    sum_pending_work = fields.Monetary(_("To Do Untaxed"), readonly=True, store=True, compute="_compute_sum_pending_work")

