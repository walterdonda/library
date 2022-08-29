from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    book_ids = fields.Many2many(
        "library.book",
        string="Libros escritos"
    )