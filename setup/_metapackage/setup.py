import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-l10n-croatia",
    description="Meta package for oca-l10n-croatia Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-currency_rate_update_hr_hnb>=16.0dev,<16.1dev',
        'odoo-addon-l10n_hr_bank>=16.0dev,<16.1dev',
        'odoo-addon-l10n_hr_base>=16.0dev,<16.1dev',
        'odoo-addon-l10n_hr_city>=16.0dev,<16.1dev',
        'odoo-addon-l10n_hr_nkd>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
