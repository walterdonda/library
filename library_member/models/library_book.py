from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class Book(models.Model):

    _inherit = "library.book"

    internal_code = fields.Integer(string="Código interno")
    is_available = fields.Boolean("Está disponible para prestar?")
    isbn = fields.Char(help="Usar un ISBN-13 o un ISBN-10 válido")
    publisher_id = fields.Many2one(index=True)
    delta_un_año_un_mes = fields.Date(
        "delta",
        default=lambda self: fields.Datetime.now() + relativedelta(years=1, months=1),
    )

    @api.constrains("internal_code")
    def _constrains_internal_code(self):
        if self.internal_code < 0 or self.internal_code > 10000:
            raise ValidationError(
                "El valor del código interno debe ser un entero mayor que cero y menor que 10000"
            )
