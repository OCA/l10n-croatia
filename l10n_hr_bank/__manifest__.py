# -*- coding: utf-8 -*
# © 2018 Davor Bojkić - Bole <bole@dajmi5.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Croatia - Banking",
    "summary": "Croatia Banking localization",
    "category": "Localisation / Croatia",
    "images": [],
    "version": "10.0.0.0.1",
    "application": False,
    "author": "Odoo Community Association (OCA)"
              ", Davor Bojkić (DAJ MI 5)",
    "website": "https://github.com/OCA/l10n-croatia",
    "license": "AGPL-3",
    "depends": [
        "base_iban",
        # 'base_bank_prefix',
    ],
    "data": [
        "data/res_bank_data.xml",
        "views/res_partner_bank_view.xml",
    ],
    "qweb": [],
    "demo": [],
    "auto_install": False,
    "installable": True,
}
