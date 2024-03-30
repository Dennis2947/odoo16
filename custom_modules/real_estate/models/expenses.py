from odoo import models, fields
class Expenses(models.Model):
    _name = 'estate.expenses'
    _description = 'Real Estate Expenses'

    name = fields.Char(string='Expense Name', required=True)
    amount = fields.Float(string='Amount')
    date = fields.Date(string='Date')
    property_id = fields.Many2one(comodel_name='estate.properties', string='Property')
