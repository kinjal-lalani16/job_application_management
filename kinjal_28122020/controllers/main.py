import json
from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.addons.website_hr_recruitment.controllers.main import WebsiteHrRecruitment


class WebsiteFormJob(WebsiteForm):

    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True)
    def website_form(self, model_name, **kwargs):
        print('=======self======', self)
        res = super(WebsiteFormJob, self).website_form(model_name, **kwargs)
        if model_name == 'hr.applicant':
            rec = request.env['hr.applicant'].sudo().browse(request.session.get('form_builder_id'))
            print('\n\n\n------->>>>>>>>>>kwargs', kwargs)
            rec.write({
                'job_experience': kwargs.get('job_experience'),
                'country_id': kwargs.get('country_id'),
                'state_id': kwargs.get('state_id'),
            })
        return res

    # def insert_record(self, request, model, values, custom, meta=None):

    #     values['job_experience'] = float(custom.split(' ')[-1])
    #     custom = ''
    #     result = super(WebsiteFormJob, self).insert_record(request, model, values, custom, meta=meta)
    #     return result
    # def insert_record(self, request, model, values, custom, meta=None):
    #     print('\n\n\n\n=====values=======',custom)
    #     print('\n\n\n\n=====values=======',custom.split('\n'))
    #     a = custom.split('\n')
    #     d = {}
    #     for i in a:
    #         b = i.split(':')
    #         d[(b[0]).rstrip()]= (b[1]).lstrip()

    #     values['job_experience'] = d['job_experience']
    #     values['country_id'] = d['country_id']
    #     values['state_id'] = d['state_id']

    #     # values['experience'] = float(custom.split(' ')[-1])
    #     custom = ''
    #     result = super(WebsiteFormJob, self).insert_record(request, model, values, custom, meta=meta)
    #     return result

class JobApply(WebsiteHrRecruitment):

    @http.route('''/jobs/apply/<model("hr.job", "[('website_id', 'in', (False, current_website_id))]"):job>''', type='http', auth="public", website=True)
    def jobs_apply(self, job, **kwargs):
        country = request.env['res.country'].sudo().search([])

        # if not job.can_access_from_current_website():
        #     raise NotFound()

        error = {}
        default = {}
        if 'website_hr_recruitment_error' in request.session:
            error = request.session.pop('website_hr_recruitment_error')
            default = request.session.pop('website_hr_recruitment_default')
        return request.render("website_hr_recruitment.apply", {
            'job': job,
            'error': error,
            'default': default,
            'con': country,
        })
