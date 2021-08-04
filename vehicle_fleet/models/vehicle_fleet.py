# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import datetime
import random


class VehicleFleet(models.Model):
    _name = "vehicle.fleet"
    _description = "Vehicle Fleet"

    brand = fields.Char(string='Brand', required=True, index=True)
    model = fields.Char(string='Model', required=True, index=True)
    mileage = fields.Integer(string='Mileage', required=True, default=0)
    purchase_date = fields.Date(string='Purchase Date', default=datetime.today(),required=True)
    purchase_value = fields.Float(string='Purchase Value', required=True, default=0)
    price = fields.Float(string='Price', required=True, default=0)
    service = fields.Integer(compute='_service', store=True, string='Service', default=0)
    description = fields.Text(string='Description', translate=True)
    active = fields.Boolean(default=True, string='Active')


    @api.depends('purchase_date')
    def _service(self):
        today = datetime.now()
        for obj in self:
            pdate = obj.purchase_date
            diff = ((today.year - pdate.year) * 12 + (today.month - pdate.month)) / 6
            obj.service = diff


    @api.onchange('mileage')
    def _onchange_purchase_value(self):
        percentage = int(self.mileage / 10000)
        for i in range(percentage):
            self.price = self.price - (self.price * 0.05)

