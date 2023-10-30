
[![Runboat](https://img.shields.io/badge/runboat-Try%20me-875A7B.png)](https://runboat.odoo-community.org/builds?repo=OCA/l10n-croatia&target_branch=16.0)
[![Pre-commit Status](https://github.com/OCA/l10n-croatia/actions/workflows/pre-commit.yml/badge.svg?branch=16.0)](https://github.com/OCA/l10n-croatia/actions/workflows/pre-commit.yml?query=branch%3A16.0)
[![Build Status](https://github.com/OCA/l10n-croatia/actions/workflows/test.yml/badge.svg?branch=16.0)](https://github.com/OCA/l10n-croatia/actions/workflows/test.yml?query=branch%3A16.0)
[![codecov](https://codecov.io/gh/OCA/l10n-croatia/branch/16.0/graph/badge.svg)](https://codecov.io/gh/OCA/l10n-croatia)
[![Translation Status](https://translation.odoo-community.org/widgets/l10n-croatia-16-0/-/svg-badge.svg)](https://translation.odoo-community.org/engage/l10n-croatia-16-0/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# l10n-croatia

This repository contains basic modules for Croatia localisation.

Important note on instaling CoA modules for this repository: ahen creating the new database
DO NOT SELECT COUNTRY - If you create a database with country set, and install Invoicing app,
the first CoA module found for selected country will be installed. That means you will hava
l10n_hr module form odoo core modules.

Correct procedure steps for using alternative CoA:

- Create new database, without country set on create screen.
- Install Invoicing app
- Go to Invoicing settings page, click on : Install additional Chart of accounts,
  then select desired CoA module.
- Proceed with usual setup steps.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[currency_rate_update_hr_hnb](currency_rate_update_hr_hnb/) | 16.0.1.0.0 |  | Update exchange rates using Croatia HNB
[l10n_hr_bank](l10n_hr_bank/) | 16.0.1.0.1 |  | Croatia Banking localization
[l10n_hr_base](l10n_hr_base/) | 16.0.1.0.1 |  | Croatia base localization data
[l10n_hr_city](l10n_hr_city/) | 16.0.1.0.1 |  | Adds location data for Croatia - Cities, post offices etc.
[l10n_hr_nkd](l10n_hr_nkd/) | 16.0.1.0.1 |  | Hrvatska - Nacionalna Klasifikacija Djelatnosti

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.
