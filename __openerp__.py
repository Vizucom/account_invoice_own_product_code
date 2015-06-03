# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Own Product Code for Supplier Invoice Lines',
    'category': 'Accounting',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['product'],
    'description': """
Own Product Code for Supplier Invoice Lines
===========================================
 * By default Odoo's supplier invoice lines contain the supplier's product information in both Product and Description columns
 * With this module the Product column always shows the company's own product info, even if supplier product info exists for the product. 
""",
    'data': [],
}
