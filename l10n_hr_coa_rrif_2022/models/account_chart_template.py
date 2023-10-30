from odoo import api, models


class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"

    @api.model
    def _prepare_all_journals(self, acc_template_ref, company, journals_dict=None):
        journal_data = super(AccountChartTemplate, self)._prepare_all_journals(
            acc_template_ref, company, journals_dict
        )
        for journal in journal_data:
            if (
                journal["type"] in ("sale", "purchase")
                and company.country_id.code == "HR"
            ):
                # uvjek storno u istom brojevnom krugu!
                journal.update({"refund_sequence": False})
        return journal_data
