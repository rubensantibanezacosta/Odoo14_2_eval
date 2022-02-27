
from odoo import models, fields, api
from datetime import timedelta

class Task(models.Model):
    _inherit = 'project.task'
    
    @api.model
    
    
    def create(self, values):
        res= super(Task, self).create(values)
    
        nuevo1= self.env['mail.activity'].create({
            'user_id': res.user_id.id,
            'res_model_id': res.project_id.alias_model_id.id,
            'res_id': res.id,
            'date_deadline': fields.Date.today(),
            'res_name': res.name,
            'note': "<p>TE CREÉ UNA TAREA................</p>",
            'summary': "TareaNueva.",
            'activity_type_id':4, #actividad de tipo ToDo
            })
    
        return res
    
