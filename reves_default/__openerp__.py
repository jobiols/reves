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
    'name': 'Reves',
    'version': '8.0.4.0',
    'category': 'Tools',
    'summary': 'Customización Ramos Revestimientos',
    'author': 'jeo Software',
    'depends': [
        'l10n_ar_base',  # modulo base para localización argentina
        'vertical_ceramicas',  # modulo vertical de mayoristas de ceramicas
        'disable_openerp_online',  # elimina referencias a odoo online
        'account_cancel',  # Check en los diarios para cancelar asientos
        'hide_product_variants',  # oculta las variantes
        'invoice_order_by_id',  # ordena facturas ultima arriba
        #     'partner_search', # permite buscar partners por varios criterios
        'account_journal_sequence',  # secuencia para ordenar diarios
        # 'account_statement_move_import' # imprtar apuntes extr bancarios
        # 'po_custom_reports',        # dependencia requerida
        # 'custom_vat_ledger',        # dependencia requerida
        'account_invoice_tax_wizard',  # insercion manual impuestos en compras
        # 'ticket_citi_fix',   # corrige citi para pv impresor fiscal
        'product_unique_default_code',  # impide duplicar default_code
        'hide_messaging',  # oculta menu de mensajeria
        'voucher_payment_check_fix',  # no cheq propios en med de pago cliente
        'account_invoice_tax_auto_update',  # autocalcula impuestos al salvar
        'server_mode',  # disable functions when running databases on debug

        # apps agregadas
        'fleet',  # maneja flota de autos
        'account_transfer',  # permite hacer transferencia entre cuentas
        'web_export_view',  # reportes en excel de cualquier vista.
        'im_chat',  # mensajeria instantanea entre usuarios de odoo
        'l10n_ar_aeroo_sale',
        'l10n_ar_aeroo_purchase',
        'l10n_ar_aeroo_einvoice',
        'l10n_ar_aeroo_stock',
        'l10n_ar_aeroo_voucher',
        'l10n_ar_fe_qr',

        # modulos para multistore
        'account_multi_store',
        'stock_multi_store',

        # impresora fiscal epson.
        'l10n_ar_fpoc',
        'fpoc',
        'product',

        # someday
        # 'currency_rate_update' # actualiza tipo de cambio
        # 'sale_order_recalculate_prices',  # recalcular precios en SOrder
    ],
    'data': [
        'views/custom_reports.xml',
        'views/product_kanban_view.xml',
    ],
    'test': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'reves', 'branch': '8.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '8.0'},
        {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
        {'usr': 'jobiols', 'repo': 'fiscal-printer', 'branch': '8.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-multi-store', 'branch': '8.0'},
        {'usr': 'jobiols', 'repo': 'odoo-jeo-ce', 'branch': '8.0'},
    ],
    'docker': [
        {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '9.5'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'}
    ]

}
