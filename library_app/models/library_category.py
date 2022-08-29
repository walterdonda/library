from odoo import api, fields, models
from odoo.tools.translate import translate

class BookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Categoría del libro'
    _parent_store = 'True'

    name = fields.Char(translate='True', required=True)
    parent_id = fields.Many2one(
        "library.book.category",
        "Categoría padre",
        ondelete="restrict"
        )
    
    child_ids = fields.One2many(
        "library.book.category",
        "parent_id",
        "Subcategorías"
    )
    
    parent_path = fields.Char(index=True)

 