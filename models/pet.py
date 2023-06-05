from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Pet(models.Model):
    _name = "pet.adoption.pet"
    _description = "Pet"

    name = fields.Char(string="Pet Name", required=True)
    type = fields.Char(string="Pet Type", required=True)
    age = fields.Char(string="Pet Age", required=True)
