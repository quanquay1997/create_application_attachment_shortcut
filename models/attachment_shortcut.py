# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Shortcut(models.Model):
    _inherit = 'calendar.event'
    attachment_number1 = fields.Integer(compute='action_event_attachment', string="Number of Attachments")

    @api.one
    def action_event_attachment(self):
        attachment_action = self.env.ref('base.action_attachment')
        action = attachment_action.read()[0]
        action['context'] = {'default_res_model' : "hr.applicant", 'default_res_id': self.applicant_id.id}
        action['domain'] = str(['&', ('res_model', '=', "hr.applicant"), ('res_id', 'in', [self.applicant_id.id])])
        action['search_view_id'] = (self.env.ref('hr_recruitment.ir_attachment_view_search_inherit_hr_recruitment').id,)
        return action

        # action = self.env.ref('base.action_attachment').read()[0]
        # action['context'] = {
        #     'default_res_model': self._name,
        #     'default_res_id': self.ids[0]
        # }
        # action['search_view_id'] = (self.env.ref('hr_recruitment.ir_attachment_view_search_inherit_hr_recruitment').id, )
        # action['domain'] = ['|', '&', ('res_model', '=', 'hr.job'), ('res_id', 'in', self.ids), '&', ('res_model', '=', 'hr.applicant'), ('res_id', 'in', self.mapped('application_ids').ids)]
        # return action
