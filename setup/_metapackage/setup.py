import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-l10n-croatia",
    description="Meta package for oca-l10n-croatia Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-currency_rate_update_hr_hnb>=18.0dev,<18.1dev',
        'odoo-addon-l10n_hr_bank>=18.0dev,<18.1dev',
        'odoo-addon-l10n_hr_base>=18.0dev,<18.1dev',
        'odoo-addon-l10n_hr_city>=18.0dev,<18.1dev',
        'odoo-addon-l10n_hr_nkd>=18.0dev,<18.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 18.0',
    ]
)
