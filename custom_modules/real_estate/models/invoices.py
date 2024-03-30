from odoo import models, fields
class Invoices(models.Model):
    _name = 'estate.invoices'
    _description = 'Real Estate Invoices'

    name = fields.Char(string='Invoice Name', required=True)
    amount = fields.Float(string='Amount')
    due_date = fields.Date(string='Due Date')
    property_id = fields.Many2one(comodel_name='estate.properties', string='Property')