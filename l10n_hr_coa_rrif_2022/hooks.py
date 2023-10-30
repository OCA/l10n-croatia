# author: bole@dajmi5.com

from odoo import SUPERUSER_ID, api


def _install_l10n_hr_modules(cr, registry):
    # l10n_hr_account canot be dependant on single COA,
    # install all localization needed modules from here
    # so everything is set according to needs
    env = api.Environment(cr, SUPERUSER_ID, {})
    modules = env["ir.module.module"]
    to_install = [
        "l10n_hr_account_base",  # osnovna lokalizacija računovodstva
        # 'l10n_hr_city',
        # 'l10n_hr_bank',
    ]
    for module in to_install:
        m = modules.search([("name", "=", module)], limit=1)
        if m and m.state != "installed":
            m.button_immediate_install()
