# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    scheduled_time = fields.Char(
        string='Scheduled Time',
        compute='_compute_scheduled_time_only',
        store=False,
    )

    def _compute_scheduled_time_only(self):
        for record in self:
            if record.scheduled_date:
                record.scheduled_time = record.scheduled_date.strftime('%H:%M:%S')
            else:
                record.scheduled_time = ''
