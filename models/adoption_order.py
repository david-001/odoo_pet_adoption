from odoo import api, fields, models
from datetime import date

class AdoptionOrder(models.Model):
    _name = "pet.adoption.order"
    _description = "Adoption Order"
    _rec_name = "ref"

    @api.model
    def default_get(self,vals):
        res = super(AdoptionOrder,self).default_get(vals)
        res["order_date"] = date.today()
        return res

    order_date = fields.Date(string="Order Date")
    adopter_id = fields.Many2one('pet.adoption.adopter', string="Adopter")
    ref = fields.Char(string="Order")

    adoption_order_line_ids = fields.One2many('pet.adoption.order.line', 'adoption_order_id', string="Adoption Order Lines")

    @api.model
    def create(self,vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('pet.adoption.order')
        return super(AdoptionOrder, self).create(vals)

    def write(self,vals):
        print("Order Saved")
        return super(AdoptionOrder, self).write(vals)
