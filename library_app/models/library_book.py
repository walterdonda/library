from datetime import datetime
from odoo import fields, models
import time


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libro'

    name = fields.Char(string='Título', required=True)

    isbn = fields.Char(
        string='ISBN',
        required=True)

    date_published = fields.Date(
        string='Fecha de publicación',
    )

    active = fields.Boolean(
        string='Activo?',
        default=True,
        help='Indica si el libro se encuentra en estado activo.'
    )

    image = fields.Binary(
        string='Imagen de portada',
    )

    publisher_id = fields.Many2one(
        string='Editorial',
        comodel_name='res.partner',
    )

    author_ids = fields.Many2many(
        string='Autores',
        comodel_name='res.partner',
    )

    def button_check_isbn(self):
        for book in self:
            if book.date_published:
                book.date_published = datetime.now()
        return True
