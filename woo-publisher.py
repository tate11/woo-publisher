# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeo-soft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
from woocommerce import API

"""
    Read the docs:
    https://pypi.python.org/pypi/WooCommerce
"""

wcapi = API(
    url="http://makeoverlab.com.ar",
    consumer_key="ck_66d4f2ce94e43a69011395aacde2b6a0bbc6c4d0",
    consumer_secret="cs_51c2ee4c29940c568f94063f0845c9f46fb476ba",
    wp_api=True,
    version="wc/v1"
)

# r = wcapi.get('')
# r = wcapi.get('customers')
# r = wcapi.get('products')
# r = wcapi.get('products/attributes')
# r = wcapi.get('products/categories')

def list_products(id=False):
    if id:
        r = wcapi.get('products/{}'.format(id))
        print r.json()
    else:
        r = wcapi.get('products')
        for item in r.json():
            print '-------------------------------------------------------------------------------'
            print 'id   >', item['id']
            print 'name >', item['name']
            print 'desc >', item['description']


def upload_product():
    data = {
        "name": "producto de prueba",
        "type": "simple",
        "regular_price": "221.99",
        "description": "Descripcion de prueba",
        "images": [
            {
                'id': 6049
            }
        ]
    }
    print(wcapi.post("products", data).json())


list_products(6051)
# upload_product()

{u'sold_individually': False, u'purchase_note': u'', u'weight': u'',
 u'regular_price': u'221.99', u'date_on_sale_to': u'', u'shipping_class': u'',
 u'featured': False, u'variations': [], u'images': [
    {u'src': u'http://makeoverlab.com.ar/wp-content/uploads/2016/10/T_2_front-1.jpg',
     u'name': u'servicio-bioestimulacion-rf', u'date_modified': u'2016-10-13T12:53:06',
     u'position': 0, u'date_created': u'2016-10-13T12:53:05',
     u'alt': u'Bioestimulacion con radiofrecuencia', u'id': 6049}], u'related_ids': [],
 u'menu_order': 0, u'id': 6051, u'sku': u'', u'rating_count': 0, u'shipping_class_id': 0,
 u'dimensions': {u'width': u'', u'length': u'', u'height': u''}, u'purchasable': True,
 u'shipping_taxable': True, u'reviews_allowed': True, u'download_limit': -1, u'tags': [],
 u'on_sale': False, u'_links': {
u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/6051'}],
u'collection': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products'}]},
 u'virtual': False, u'average_rating': u'0.00',
 u'price_html': u'<span class="woocommerce-Price-amount amount"><span class="woocommerce-Price-currencySymbol">&#36;</span>221,99</span>',
 u'downloadable': False, u'parent_id': 0, u'catalog_visibility': u'visible',
 u'backordered': False, u'short_description': u'', u'sale_price': u'', u'type': u'simple',
 u'downloads': [], u'grouped_products': [], u'status': u'publish', u'backorders': u'no',
 u'description': u'<p>Descripcion de prueba</p>\n', u'shipping_required': True,
 u'price': u'221.99', u'button_text': u'', u'manage_stock': False,
 u'stock_quantity': None, u'in_stock': True, u'attributes': [], u'date_on_sale_from': u'',
 u'slug': u'producto-de-prueba', u'categories': [],
 u'permalink': u'http://makeoverlab.com.ar/producto/producto-de-prueba/',
 u'default_attributes': [], u'name': u'producto de prueba',
 u'date_modified': u'2016-10-13T13:31:39', u'tax_class': u'', u'total_sales': 0,
 u'upsell_ids': [], u'cross_sell_ids': [], u'download_expiry': -1,
 u'backorders_allowed': False, u'tax_status': u'taxable',
 u'date_created': u'2016-10-13T13:31:39', u'download_type': u'standard',
 u'external_url': u''}
