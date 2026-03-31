from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    allow_multi_user_to_start_task = fields.Boolean(string="Allow Multi User To Start Task", config_parameter='task_timer_ucs.allow_multi_user_to_start_task')
