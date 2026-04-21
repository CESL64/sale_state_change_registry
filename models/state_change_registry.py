from odoo import fields, models


class StateChangeRegistry(models.Model):
    _inherit = "state.change.registry"

    sale_id = fields.Many2one(
        comodel_name="sale.order",
        string="Orden de Venta",
    )
