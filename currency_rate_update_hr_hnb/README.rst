============================
Currency Rate Update: HNB.hr
============================

This module provides adds `Croatia HNB <https://www.hnb.hr/temeljne-funkcije/monetarna-politika/tecajna-lista/tecajna-lista>`_. currency exchange rates
provider.

Configuration
=============

To configure Croatia HNB currency rates provider :

Go to *Invoicing > Configuration > Currency update providers*
create new provider : Croatia-HNB

HNB Provides 3 rates: buy, mid and sell. By default mid rate is covered,
as it is only legaly required, but if you want to use buy or sell rate...
there is a config parameter: currency_rate_update_hr_hnb.rate_type
withe values accepted: srednji | kupovni | prodajni


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-croatia/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
