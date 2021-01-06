from odoo import fields, models,api

class HrApplicant(models.Model):
    _inherit = "hr.applicant"
    _description = "hr_applicant"

    job_experience = fields.Float(string="Total experience")
    country_id = fields.Many2one('res.country', string="Country")
    state_id = fields.Many2one('res.country.state', string="State")

    @api.model
    def get_state(self,country_id):
        print("HEllo---------caldkfjk")
        # print(f"----------country_id :- {country_id[0][2]} type : {type(country_id[0][2])}")
        states = self.env['res.country.state'].search([('country_id','=',int(country_id))])
        print("-------states-------",states)
        s_final = {}
        for state in states:
            s_final[state.id]=state.name
        print(f"\n\n---------s_final:- {s_final} \n\n")
        return s_final
