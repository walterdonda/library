from odoo import fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libro'
    _order= 'date_published ASC, name'

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

    price = fields.Float(digits=(12,2), string= "Precio del libro")

    def button_check_isbn(self):
        self.active = False
