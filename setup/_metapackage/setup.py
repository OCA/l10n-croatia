import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-l10n-croatia",
    description="Meta package for oca-l10n-croatia Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-l10n_hr_bank',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
