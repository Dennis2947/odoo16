from odoo import models, fields
class Inventory(models.Model):
    _name = 'estate.inventory'
    _description = 'Real Estate Inventory'

    name = fields.Char(string='Inventory Name', required=True)
    quantity = fields.Integer(string='Quantity')
    property_id = fields.Many2one(comodel_name='estate.properties', string='Property')