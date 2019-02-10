from odoo import api, exceptions, fields, models

class CheckoutMassMessage(models.TransientModel):
    _name = 'library.checkout.massmessage'
    _description = 'Send Message to Borrowers'
    checkout_ids = fields.Many2many(
        'library.checkout',
        string='Checkouts')
    message_subject = fields.Char()
    message_body = fields.Html()

@api.model
def default_get(self, field_names):
    defaults = super().default_get(field_names)
    checkout_ids = self.env.context['active_ids']
    defaults['checkout_ids'] = checkout_ids
    return defaults
    
