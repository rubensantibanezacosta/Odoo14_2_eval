# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencias_incidencias(models.Model):
    _name = 'incidencias.incidencias'
    _description = 'incidencias.incidencias'
    _inherit=['mail.thread','mail.activity.mixin']

   
    name = fields.Integer(string="Número de incidencias")
    municipio = fields.Many2one("incidencias.municipios", string="Municipio", required=True, ondelete="cascade")
    fecha = fields.Date(string="Fecha")
    descripcion = fields.Many2one("res.users",string="Usuario que atiende la incidencia",required=True,ondelete="cascade")
    cliente = fields.Many2one("res.partner", string="Cliente", required=True, ondelete="cascade")
    
 #  @api.model
    
  #  def create(self, values):
#    res= super(incidencias_incidencias, self).create(values)
        
    
 #       nuevo1= self.env['mail.activity'].create({
  #          'user_id': 2,
   #         'res_model_id': 489,
    #        'res_id': 32,
     #       'date_deadline': fields.Date.today(),
      #      'res_name':"project.task",
       #     'note': "<p>TE CREÉ UNA TAREA................</p>",
        #    'summary': "TareaNueva.",
         #   'activity_type_id':4, #actividad de tipo ToDo
          #  })
    
       # return res
         
    
    


class incidencias_municipios(models.Model):
    _name = 'incidencias.municipios'
    _description = 'incidencias.municipios'

    name = fields.Char(string="Nombre")
    habitantes = fields.Integer(string = "Habitantes")
    imagen = fields.Binary(string="Mapa del municipio")
    superficie = fields.Integer(string="Superficie")
    densidad_poblacion = fields.Float(string="Densidad de población", compute="_densidadpoblacion", store=True)
    incidencias = fields.One2many("incidencias.incidencias", "municipio", string="Incidencias")

    @api.depends('habitantes',"superficie")
    def _densidadpoblacion(self):
        for record in self:
            if record.superficie > 0:
                record.densidad_poblacion = record.habitantes / record.superficie

    

class incidencias_clientes(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    incidencias = fields.One2many("incidencias.incidencias", "cliente", string="Incidencias")
    sign=fields.Binary(string="Firma");