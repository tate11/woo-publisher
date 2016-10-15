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
        r = self._wcapi.get('products/categories?per_page=100')
        categories = []
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
