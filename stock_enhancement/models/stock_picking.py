# -*- coding: utf-8 -*-

from odoo import models, fields, api
from pytz import timezone, UTC


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
                # Get company timezone, fallback to UTC
                company_tz = record.company_id.partner_id.tz or 'UTC'
                # Convert from UTC to company timezone
                local_dt = record.scheduled_date.replace(tzinfo=UTC).astimezone(timezone(company_tz))
                record.scheduled_time = local_dt.strftime('%H:%M:%S')
            else:
                record.scheduled_time = ''
