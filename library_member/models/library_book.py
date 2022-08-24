from odoo import fields, models

class Book(models.Model):

    _inherit = 'library.book'

    is_available = fields.Boolean("Está disponible para prestar?") 
    