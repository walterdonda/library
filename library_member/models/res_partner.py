from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    member_id = fields.One2many(
        "library.member",
        "partner_id",
        string= "miembro"
    )
    