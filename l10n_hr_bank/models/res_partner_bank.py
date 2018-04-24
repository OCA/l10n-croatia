# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    acc_purpose = fields.Selection([
        ('tek', 'Personal salary'),
        ('ziro', 'Secondary income'),
        ('prot', 'Protected'),
        ('other', 'Other')
    ], 'Account purpose', help="""
    Personal salary - regular account for receiving salary
    Secondary income - personal account for secondary income
    Protected - Special account for law-protected part of salary""")
    purpose_required = fields.Boolean(
        compute='_compute_purpose_required',
    )

    @api.depends('partner_id', 'company_id')
    def _compute_purpose_required(self):
        for acc in self:
            acc.purpose_required = acc.acc_number.startswith('HR') and \
                acc.company_id.country_id and \
                acc.company_id.country_id.code == "HR" and \
                not acc.partner_id.is_company
