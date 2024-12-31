# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pw_total_product_uom_qty = fields.Float(string="Total Demand Qty", compute='_compute_pw_total_product_uom_qty')
    pw_total_qty_delivered = fields.Float(string="Total Delivered Qty", compute='_compute_pw_total_qty_delivered')
    pw_total_qty_invoiced = fields.Float(string="Total Invoiced Qty", compute='_compute_pw_total_qty_invoiced')
    pw_remaining_delivery = fields.Float(string="Pending Delivery Qty", compute="_compute_pw_remaining_delivery")
    pw_remaining_invoice = fields.Float(string="Pending Invoice Qty", compute="_compute_pw_remaining_invoice")

    @api.depends('order_line.product_uom_qty')
    def _compute_pw_total_product_uom_qty(self):
        for order in self:
            order.pw_total_product_uom_qty = sum(order.order_line.mapped('product_uom_qty'))

    @api.depends('order_line.qty_delivered')
    def _compute_pw_total_qty_delivered(self):
        for order in self:
            order.pw_total_qty_delivered = sum(order.order_line.mapped('qty_delivered'))

    @api.depends('order_line.qty_invoiced')
    def _compute_pw_total_qty_invoiced(self):
        for order in self:
            order.pw_total_qty_invoiced = sum(order.order_line.mapped('qty_invoiced'))

    @api.depends('order_line.product_uom_qty', 'order_line.qty_delivered')
    def _compute_pw_remaining_delivery(self):
        for order in self:
            delivery_qty = sum(order.order_line.filtered(lambda x: x.product_id.type != 'service').mapped('product_uom_qty'))
            delivered_qty = sum(order.order_line.mapped('qty_delivered'))
            order.pw_remaining_delivery = delivery_qty - delivered_qty

    @api.depends('pw_total_product_uom_qty', 'pw_total_qty_invoiced')
    def _compute_pw_remaining_invoice(self):
        for order in self:
            order.pw_remaining_invoice = order.pw_total_product_uom_qty - order.pw_total_qty_invoiced
