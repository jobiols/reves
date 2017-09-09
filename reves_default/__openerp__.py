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

{
    'name': 'Ramos Revestimientos',
    'version': '8.0.1.1',
    'category': 'Tools',
    'summary': 'Customización Ramos Revestimientos',
    'description': """

Customización Ramos Revestimientos
==================================

NO INSTALAR, INCLUYE LA VERTICALIZACION

""",
    'author': 'jeo Software',
    'depends': [
        'l10n_ar_base',  # modulo base para localización argentina
        'base_vat_unique',  # evita que duplique cuit
        'base_vat_dni',     # validaciones para DNI / CUIT
        # 'base_vat_unique_parent',  # evita que duplique cuit en multicompañia
        'disable_openerp_online',  # elimina referencias a odoo online
        'account_cancel',  # Muestra el check en los diarios que permite cancelar asientos
        'hide_product_variants',  # oculta las variantes
        'im_chat',  # mensajeria instantanea entre usuarios de odoo
        #        'express_checkout',         # Facturación express
        'invoice_order_by_id',  # ordena facturas ultima arriba
        #        'sale_order_recalculate_prices',  # agrega boton para recalcular precios
        #        'consult_product_price',    # consulta de precios
        #        'partner_search',            # permite buscar partners por varios criterios
        'account_journal_sequence',  # agrega un campo de secuencia en el diario para ordenarlos
        # 'account_statement_move_import'  # agrega boton de importar aputnes en extractos bancarios
        'l10n_ar_aeroo_sale',  # dependencia requerida
        'l10n_ar_aeroo_purchase',  # dependencia requerida
        'l10n_ar_aeroo_einvoice',  # dependencia requerida
        'l10n_ar_aeroo_stock',  # dependencia requerida
        'l10n_ar_aeroo_voucher', # dependencia requerida
        #        'po_custom_reports',        # dependencia requerida
        #        'custom_vat_ledger',        # dependencia requerida
        #        'odoo_argentina_fix',       # patch a la localización
        #        'account_invoice_tax_add',  # agrega insercion manual de impuestos para factura de compras
        #        'ticket_citi_fix',          # corrige citi para pv impresor fiscal
        'product_unique_default_code',  # impide que se duplique el default_code
        'hide_messaging',  # oculta el menu de mensajeria
#        'base_multi_store',  # agrega capacidad de multitienda analogo a multicompañia
        'account_multi_store', 'base_multi_store', 'stock_multi_store',  # capacidad de limitar los diarios segun los stores (repo journal-constraint)
        'voucher_payment_check_fix',  # evita que aparezca cheques propios en medios de pago de cliente
        'account_invoice_tax_auto_update', # autocalcula los impuestos al salvar asi no hay que hacer el update

        # impresora fiscal epson
        'fpoc',
        'l10n_ar_fpoc'
    ],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'views/custom_reports.xml',
        'views/res_product.xml',
        'views/account_tax_view.xml',
        'views/sale_view.xml',
        'views/pricelist_view.xml',
        'stock_report.xml',
        'views/report_stockpicking.xml',
        'views/res_company.xml',
        'views/account_invoice.xml'
    ],
    'test': [

    ],
    'installable': False,
    'application': True,
    'auto_install': False,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
