from odoo import fields, models


class Member(models.Model):

    _inherit = ["mail.thread", "mail.activity.mixin"]

    _name = "library.member"

    _description = "Library Member"
    
    card_number = fields.Char()

    partner_id = fields.Many2one(
        "res.partner", delegate=True, ondelete="cascade", required=True
    )
