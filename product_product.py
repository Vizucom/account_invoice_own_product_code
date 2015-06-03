# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class product_product(osv.Model):

    _inherit = "product.product"

    def name_get(self, cr, user, ids, context=None):
        
        if context is None:
            context = {}
                
        if context.get('type', False) == 'in_invoice' and context.get('partner_id', False):
            ctx_no_partner = context.copy()
            ctx_no_partner.pop('partner_id', None)
            return super(product_product, self).name_get(cr, user, ids, ctx_no_partner)
        else:
            return super(product_product, self).name_get(cr, user, ids, context)