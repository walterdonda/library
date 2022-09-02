from odoo import fields, models


class Member(models.Model):

    _inherit = ["mail.thread", "mail.activity.mixin"]

    _name = "library.member"

    _description = "Library Member"

    card_number = fields.Char(string="Número de socio")

    partner_id = fields.Many2one(
        "res.partner", delegate=True, ondelete="cascade", required=True
    )

    _sql_constraints = [
        (
            "card_number_unique",
            "UNIQUE(card_number)",
            "El número de socio debe ser único",
        ),
    ]
