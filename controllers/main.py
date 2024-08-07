from odoo import http
from odoo.http import request

class ExternalInventoryController(http.Controller):

    @http.route('/external_inventory', auth='user', type='http', website=True)
    def index(self, **kw):
        products = request.env['product.product'].sudo().search([])
        quants = request.env['stock.quant'].sudo().search([])
        return request.render('external_inventory_view.index', {'products': products, 'quants': quants})
