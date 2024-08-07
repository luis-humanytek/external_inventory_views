# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'External Inventory View',
    'version': '1.0',
    'depends': ['base', 'stock'],
    'data': [
        'security/external_inventory_security.xml',
        'security/ir.model.access.csv',
        'views/external_inventory_views.xml',
    ],
}

