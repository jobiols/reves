# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
##############################################################################
from openerp import SUPERUSER_ID
from openerp.osv import osv
from openerp.tools import float_compare
from openerp.tools.translate import _


class sale_order_line(osv.osv):
    _inherit = 'sale.order.line'

    def product_id_change_with_wh(self, cr, uid, ids, pricelist, product, qty=0,
                                  uom=False, qty_uos=0, uos=False, name='', partner_id=False,
                                  lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False,
                                  flag=False, warehouse_id=False, context=None):
        context = context or {}
        product_uom_obj = self.pool.get('product.uom')
        product_obj = self.pool.get('product.product')
        warning = {}
        # UoM False due to hack which makes sure uom changes price, ... in product_id_change
        res = self.product_id_change(cr, uid, ids, pricelist, product, qty=qty,
                                     uom=False, qty_uos=qty_uos, uos=uos, name=name, partner_id=partner_id,
                                     lang=lang, update_tax=update_tax, date_order=date_order, packaging=packaging,
                                     fiscal_position=fiscal_position, flag=flag, context=context)

        if not product:
            res['value'].update({'product_packaging': False})
            return res

        # set product uom in context to get virtual stock in current uom
        if 'product_uom' in res.get('value', {}):
            # use the uom changed by super call
            context = dict(context, uom=res['value']['product_uom'])
        elif uom:
            # fallback on selected
            context = dict(context, uom=uom)

        # update of result obtained in super function
        product_obj = product_obj.browse(cr, uid, product, context=context)
        res['value'].update(
                {'product_tmpl_id': product_obj.product_tmpl_id.id, 'delay': (product_obj.sale_delay or 0.0)})

        # Calling product_packaging_change function after updating UoM
        res_packing = self.product_packaging_change(cr, uid, ids, pricelist, product, qty, uom, partner_id, packaging,
                                                    context=context)
        res['value'].update(res_packing.get('value', {}))
        warning_msgs = res_packing.get('warning') and res_packing['warning']['message'] or ''

        if product_obj.type == 'product':
            # determine if the product needs further check for stock availibility
            is_available = self._check_routing(cr, uid, ids, product_obj, warehouse_id, context=context)

            # check if product is available, and if not: raise a warning, but do this only for products that aren't processed in MTO
            if not is_available:
                uom_record = False
                if uom:
                    uom_record = product_uom_obj.browse(cr, uid, uom, context=context)
                    if product_obj.uom_id.category_id.id != uom_record.category_id.id:
                        uom_record = False
                if not uom_record:
                    uom_record = product_obj.uom_id
                compare_qty = float_compare(product_obj.virtual_available, qty, precision_rounding=uom_record.rounding)
                if compare_qty == -1:
                    usr_obj = self.pool['res.users'].browse(cr, uid, uid, context=context)
                    location = usr_obj.store_id.name if usr_obj.store_id.name else u'toda la compañia'
#                    self.calc_virtual_stock(cr, uid, product, uom_record, context)
                    warn_msg = u'Querés vender {} {}\n pero solo tenés {} {} disponible en {}!\n El stock en mano es {} {}. (sin tener en cuenta lo reservado)'.format(
                            qty, uom_record.name,
                            max(0, product_obj.virtual_available), uom_record.name,
                            location,
                            max(0, product_obj.qty_available), uom_record.name)
                    warning_msgs += _("Not enough stock ! : ") + warn_msg + "\n\n"

        # update of warning messages
        if warning_msgs:
            warning = {
                'title': ('No hay stock!'),
                'message': warning_msgs
            }
        res.update({'warning': warning})
        return res

    def calc_virtual_stock(self, cr, uid, product_id, uom_record, context):
        """ Esto imprime las existencias por almacen, pero deja algo mal porque cuando sale revienta.
        """
        print 'product id', product_id
        product_obj = self.pool['product.product'].browse(cr, uid, [product_id], context=context)
        print 'product name', product_obj.name

        usr_obj = self.pool['res.users']
        usr = usr_obj.browse(cr, uid, uid, context=context)
        # guardar la store
        tmp_store = usr.store_id.id
        print 'guardo esto',tmp_store

        # obtener todas las stores
        store_ids = self.pool['res.store'].search(cr, SUPERUSER_ID, [('parent_id', '<>', False)], context=context)
        print 'usr', usr.name
        for store_id in store_ids:
            store = self.pool['res.store'].browse(cr, SUPERUSER_ID, store_id, context=context)
            print 'guardo esto>', store.id
            usr_obj.write(cr, SUPERUSER_ID, uid, {'store_id': store.id})
            location = usr.store_id.name if usr.store_id.name else u'toda la compañia'
            print 'calculando stock virtual ----------------------------------------', store.name, store.id
            print 'prod>', product_obj.default_code
            print 'virtual', product_obj.virtual_available, uom_record.name
            print 'real   ', product_obj.qty_available, uom_record.name
            print 'ubicacion', location
            print '-'

        #usr_obj.write(cr, SUPERUSER_ID, uid, {'store_id': tmp_store})
        print '<<<<<<<<<<<<<<<<<<<<<<'

