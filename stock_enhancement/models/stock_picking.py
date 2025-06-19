# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    scheduled_time = fields.Datetime('Scheduled time', compute='_compute_scheduled_time_only', )

    def _compute_scheduled_time_only(self):
        for record in self:
            if record.scheduled_date:
                record.scheduled_time = fields.Datetime.to_string(record.scheduled_date)[11:19]
            else:
                record.scheduled_time = ''
