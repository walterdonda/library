from operator import index
from odoo import fields, models
from dateutil.relativedelta import relativedelta


class Book(models.Model):

    _inherit = "library.book"

    is_available = fields.Boolean("Está disponible para prestar?")
    isbn = fields.Char(help="Usar un ISBN-13 o un ISBN-10 válido")
    publisher_id = fields.Many2one(index=True)
    delta_un_año_un_mes = fields.Date(
        "delta",
        default=lambda self: fields.Datetime.now() + relativedelta(years=1, months=1),
    )
