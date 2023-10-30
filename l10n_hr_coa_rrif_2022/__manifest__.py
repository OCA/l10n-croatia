{
    "name": "Croatia - Accounting (RRIF 2021)",
    "version": "16.0.1.0.0",
    "author": "DAJ MI 5, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-croatia",
    "category": "Accounting/Localizations/Account Charts",
    "license": "AGPL-3",
    "depends": [
        "account",
        "base_vat",
        # "l10n_multilang",  # not working good!
    ],
    "data": [
        "data/l10n_hr_chart_data.xml",
        "data/account.account.template.csv",
        "data/account.group.template.csv",  # Account groups full structure for analytic
        "data/account.tax.group.csv",
        "data/account_chart_tag_data.xml",
        "data/account_tax_report_data.xml",
        "data/account_tax_template_data.xml",
        "data/account_fiscal_position_data.xml",
        "data/account_chart_template_data.xml",
    ],
    "demo": [
        "demo/demo_company.xml",
    ],
}
