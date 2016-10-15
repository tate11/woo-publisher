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

class woo_product():
    def __init__(self, wcapi):
        self._wcapi = wcapi

    def _chck_exist(self, prod):
        ret = self._wcapi.get('products/{}'.format(prod.woo_id))
        return ret.status_code <> 404

    def _do_update(self, prod):
        data = self._encode(prod)
        ret = self._wcapi.put('products/{}'.format(prod.woo_id), data)
        print 'update', ret.status_code, prod.name
        return ret.status_code == 200

    def _do_create(self, prod):
        data = self._encode(prod)
        ret = self._wcapi.post('products', data)
        print 'create', ret.status_code, prod.name
        if ret.status_code == 201:
            print 'actualiza woo id', prod.woo_id, ret.json()['id']
            prod.woo_id = ret.json()['id']
        else:
            print ret.json()['message']
            print prod.name, prod.default_code
            exit()

    def update(self, prod):
        if self._chck_exist(prod):
            self._do_update(prod)
        else:
            self._do_create(prod)

    def _encode(self, prod):
        ret = {}
        ret['name'] = prod.name
        if prod.description:
            ret['description'] = prod.description
        ret['type'] = 'simple'
        ret['regular_price'] = str(prod.lst_price)
        ret['sku'] = prod.default_code
        categories = []
        if prod.woo_categ:
            categories.append({u'id': prod.woo_categ.woo_id})
        if prod.woo_subcateg:
            categories.append({u'id': prod.woo_subcateg.woo_id})
        ret['categories'] = categories
        return ret

    def list_products(self, id=False):
        if id:
            r = self._wcapi.get('products/{}'.format(id))
            print r.json()
        else:
            r = self._wcapi.get('products')
            for item in r.json():
                print '-------------------------------------------------------------------------------'
                print 'id   >', item['id']
                print 'name >', item['name']
                print 'desc >', item['description']

    def list_categories(self):
        r = self._wcapi.get('products/categories')
        categories = []
        print r
        print r.status_code
        print r.headers['Link']
        print r.encoding
        print r.text


        for cat in r.json():
            if cat['parent'] <> 0:
                name = '--- ' + cat['name']
            else:
                name = cat['name']
            categories.append({
                'slug': cat['slug'],
                'woo_id': cat['id'],
                'name': name
            })
        return categories  # r = wcapi.get('')

# r = wcapi.get('customers')
# r = wcapi.get('products')
# r = wcapi.get('products/attributes')
# r = wcapi.get('products/categories')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:



[{u'count': 0,
  u'description': u'',
  u'parent': 84,
  u'image': [],
  u'display': u'default',
  u'_links': {
  u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/98'}],
  u'up': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/84'}],
  u'collection': [
      {u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories'}]},
  u'id': 98,
  u'menu_order': 0,
  u'slug': u'accesorios',
  u'name': u'Accesorios'},

 {u'count': 0, u'description': u'', u'parent': 82, u'image': [], u'display': u'default',
  u'_links': {
  u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/85'}],
  u'up': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/82'}],
  u'collection': [
      {u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories'}]},
  u'id': 85, u'menu_order': 0, u'slug': u'bases', u'name': u'Bases'},

 {u'count': 0, u'description': u'', u'parent': 84, u'image': [], u'display': u'default',
  u'_links': {
  u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/95'}],
  u'up': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/84'}],
  u'collection': [
      {u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories'}]},
  u'id': 95, u'menu_order': 0, u'slug': u'brochas', u'name': u'Brochas'},

 {u'count': 0, u'description': u'', u'parent': 84, u'image': [], u'display': u'default',
  u'_links': {
  u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/97'}],
  u'up': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/84'}],
  u'collection': [
      {u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories'}]},
  u'id': 97, u'menu_order': 0, u'slug': u'combos', u'name': u'Combos'},

 {u'count': 0, u'description': u'', u'parent': 82, u'image': [], u'display': u'default',
  u'_links': {
  u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/86'}],
  u'up': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/82'}],
  u'collection': [
      {u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories'}]},
  u'id': 86, u'menu_order': 0, u'slug': u'correctores', u'name': u'Correctores'},
 {u'count': 0, u'description': u'', u'parent': 0, u'image': [], u'display': u'default',
  u'_links': {
  u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/82'}],
  u'collection': [
      {u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories'}]},
  u'id': 82, u'menu_order': 0, u'slug': u'cosmeticos', u'name': u'Cosm\xe9ticos'},
 {u'count': 0, u'description': u'', u'parent': 82, u'image': [], u'display': u'default',
  u'_links': {
  u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/88'}],
  u'up': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/82'}],
  u'collection': [
      {u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories'}]},
  u'id': 88, u'menu_order': 0, u'slug': u'delineadores', u'name': u'Delineadores'},
 {u'count': 0, u'description': u'', u'parent': 0, u'image': [], u'display': u'default',
  u'_links': {
  u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/83'}],
  u'collection': [
      {u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories'}]},
  u'id': 83, u'menu_order': 0, u'slug': u'higiene-facial', u'name': u'Higiene facial'},
 {u'count': 0, u'description': u'', u'parent': 83, u'image': [], u'display': u'default',
  u'_links': {
  u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/92'}],
  u'up': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/83'}],
  u'collection': [
      {u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories'}]},
  u'id': 92, u'menu_order': 0, u'slug': u'humectacion-hidratacion',
  u'name': u'Humectaci\xf3n / Hidrataci\xf3n'},

 {u'count': 0, u'description': u'', u'parent': 82, u'image': [], u'display': u'default',
  u'_links': {
  u'self': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/89'}],
  u'up': [{u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories/82'}],
  u'collection': [
      {u'href': u'http://makeoverlab.com.ar/wp-json/wc/v1/products/categories'}]},
  u'id': 89, u'menu_order': 0, u'slug': u'labiales', u'name': u'Labiales'}

 ]
