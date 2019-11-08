# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import models, fields


class StockPackageStorageType(models.Model):

    _name = 'stock.package.storage.type'
    _description = 'Stock package storage type'

    name = fields.Char(required=True)
    stock_location_storage_type_id = fields.Many2one(
        'stock.location.storage.type'
    )
    product_packaging_ids = fields.One2many(
        'product.packaging', 'stock_package_storage_type_id',
    )
