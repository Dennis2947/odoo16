from odoo import models, fields
class Tenants(models.Model):
    _name = 'estate.tenants'
    _description = 'Real Estate Tenants'

    name = fields.Char(string='Tenant Name', required=True)
    contact_information = fields.Text(string='Contact Information')
    property_id = fields.Many2one(comodel_name='estate.properties', string='Property')