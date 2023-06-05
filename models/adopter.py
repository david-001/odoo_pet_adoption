from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Adopter(models.Model):
    _name = "pet.adoption.adopter"
    _description = "Adopter"

    name = fields.Char(string="Adopter Name", required=True)
    email = fields.Char(string="Email", required=True)