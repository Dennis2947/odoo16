from odoo import fields, models
class Properties(models.Model):
    _name = 'estate.properties'
    _description = 'Real Estate Properties'

    name = fields.Char(string='Property Name', required=True)
    location = fields.Char(string='Location', required=True)
    description = fields.Text(string='Description')
    date_availability = fields.Date(string='Availability Date')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Number of Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string='Garden Orientation')