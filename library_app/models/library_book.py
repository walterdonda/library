from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Book(models.Model):
    """
    Catálogo de libros con sus características.
    """

    _name = "library.book"
    _description = "Book"
    _order = "name, date_published desc"
    _table = "library_book"
    _log_access = True
    _auto = True

    # String fields:
    name = fields.Char(
        "Título",
        default=None,
        help="Título del libro.",
        readonly=False,
        required=True,
        index=True,
        copy=False,
    )
    isbn = fields.Char("ISBN")
    book_type = fields.Selection(
        [
            ("paper", "Tapa blanda"),
            ("hard", "Tapa dura"),
            ("electronic", "Electrónico"),
            ("other", "otro"),
        ],
        "Tipo de libro",
    )
    notes = fields.Text("Nota interna")
    description = fields.Html("Descripción")

    # Numeric fields:
    copies = fields.Integer(default=1)
    avg_rating = fields.Float("Rating promedio", (3, 2))
    price = fields.Monetary("Precio de venta al público", "currency_id")
    currency_id = fields.Many2one("res.currency")  # price helper

    # Date and time fields:
    date_published = fields.Date(string="Fecha de publicación")
    last_borrow_date = fields.Datetime(
        "Última vez que se prestó el libro",
        default=lambda self: fields.Datetime.now(),
    )

    # Other fields:
    active = fields.Boolean("Activo?", default=True)
    image = fields.Binary("Imagen de portada")

    # Relational Fields
    publisher_id = fields.Many2one("res.partner", string="Editorial", index=True)
    author_ids = fields.Many2many("res.partner", string="Autores")

    @api.depends("publisher_id.country_id")
    def _compute_publisher_country(self):
        for book in self:
            book.publisher_country_id = book.publisher_id.country_id

    def _inverse_publisher_country(self):
        for book in self:
            book.publisher_id.country_id = book.publisher_country_id

    def _search_publisher_country(self, operator, value):
        return [("publisher_id.country_id", operator, value)]

    publisher_country_id = fields.Many2one(
        "res.country",
        string="País de la editorial",
        compute="_compute_publisher_country",
        inverse="_inverse_publisher_country",
        search="_search_publisher_country",
    )

    _sql_constraints = [
        (
            "library_book_name_date_uq",
            "UNIQUE (name, date_published)",
            "El título y la fecha de publicación ya fueron ingresados.",
        ),
        (
            "library_book_check_date",
            "CHECK (date_published <= current_date)",
            "La fecha de la publicación no puede ser en el futuro.",
        ),
    ]

    @api.constrains("isbn")
    def _constrain_isbn_valid(self):
        for book in self:
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s es un ISBN inválido" % book.isbn)

    def _check_isbn(self):
        self.ensure_one()  # Esto requiere que valide sobre un solo registro y no hago un for
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError(
                    "Por favor ingresa el ISBN para el libro titulado %s" % book.name
                )
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s El ISBN es inválido" % book.isbn)
        return True

    def map(self):
        books = self.env["library.book"].search([])
        books_mapped = books.mapped(lambda b: b)
        print(books_mapped)
