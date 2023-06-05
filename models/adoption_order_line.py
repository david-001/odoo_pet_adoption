from odoo import api, fields, models

class AdoptionOrderLine(models.Model):
    _name = "pet.adoption.order.line"
    _description = "Adoption Order Line"

    pet_id = fields.Many2one('pet.adoption.pet', string="Pet")
    type = fields.Char(related="pet_id.type", string="Pet Type")
    age = fields.Char(related="pet_id.age", string="Pet Age")

    adoption_order_id = fields.Many2one('pet.adoption.order', string="Adoption Order")
    order_date = fields.Date(related="adoption_order_id.order_date")
    adopter_id = fields.Many2one(related="adoption_order_id.adopter_id")