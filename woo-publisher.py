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
from product import woo_product
import odoorpc

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

PASSWORD = raw_input('Enter password: ')


login = {
    #    'server': '52.205.148.95',
    'server': 'localhost',
    'port': 8068,
    'database': 'makeover_datos',
    'username': 'admin',
    'password': PASSWORD,
}

# conectar con odoo, proveer credenciales
odoo = odoorpc.ODOO(login.get('server'), port=login.get('port'))
odoo.login(login.get('database'), login.get('username'), login.get('password'))

woo = woo_product(wcapi)

"""
# Copiar categorias de woo a odoo, OJOOO borra todo y lo vuelve a poner
# hacerlo solo la primera vez OJOOO
categories = odoo.env['curso.woo.categ']
ids = categories.search([])
for cat in categories.browse(ids):
    cat.unlink()
for cat in woo.list_categories():
    print cat
    categories.create(cat)
exit()
"""

# copiar productos de odoo a woo y bajar las imagenes
# las imagenes quedan en img/
# copiarlas con:
# scp *.png jobiols@hostgator:~/public_html/armonia/wp-content/uploads/2016/10/

prod = odoo.env['product.product']
# seleccionar que tenga woo_categ y que tenga imagen
ids = prod.search(
    [('woo_categ', '<>', False),
     ('image','<>',False),
     ('default_code','<>',False),
     ('description','<>',False),
     ('woo_id','=',False)], limit=10)
for pro in prod.browse(ids):
    woo.update(pro)
    filename = './img/default_code_{}.png'.format(pro.default_code)
    with open(filename, 'wb') as f:
        f.write(pro.image.decode('base64'))
