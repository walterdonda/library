from odoo import fields, models

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libro'
    
    name = fields.Char(string='Título', required=True)
    
    isbn = fields.Char(
        string='ISBN',
        required=True)
    
    date_release = fields.Date(
        string='Fecha de publicación',
    )

    
    active = fields.Boolean(
        string='Activo?',
        default = True,
        help='Indica si el libro se encuentra en estado activo.'
        )
    
    
    image = fields.Binary(
        string='Imagen de portada',
    )

    
    
    

    
    
    
    
  