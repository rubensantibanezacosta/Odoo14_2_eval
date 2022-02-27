
# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api
import base64
import requests



    
class ocio_users(models.Model):
    _inherit = "res.users"
    _name = 'res.users'

    punctuation_avg = fields.Float(string = 'Puntuacion media')
    lastconnection=fields.Datetime(string = 'Ultima conexión')
    dark_mode_boolean = fields.Boolean(string="Modo oscuro", default=False)
    events=fields.One2many("ocio__open.ocio__open_events", "organizer", string="Eventos")
    
    


    #  @api.depends('value')
    #  def _value_pc(self):
    #      for record in self:
    #          record.value2 = float(record.value) / 100

class ocio__open_ocio__open_events(models.Model):
    _name = 'ocio__open.ocio__open_events'
    _description = 'ocio__open.ocio__open_events'
    _inherit=['mail.thread','mail.activity.mixin']

    
    tittle = fields.Char(string="Titulo", required=True)
    date = fields.Datetime(string="Fecha y Hora" , required=True)
    zone = fields.Selection([('GC', 'Gran Canaria'),('TNF', 'Tenerife'),('VIRTUAL', 'Virtual'),('Others', 'Otros')],default="GC", string="Zona" , required=True)
    place = fields.Char(string="Rol")
    description = fields.Text(string="Descripción")
    punctuation_avg = fields.Float(string="Puntuacion media", default=0, readonly=True)
    organizer = fields.Many2one("res.users", string="Organizador" , ondelete="cascade", required=True)
    image_id = fields.Many2one("ocio__open.ocio__open_images", string="Imagen", null=True , ondelete="cascade")
    createdAt=fields.Date(string="Fecha de registro", auto_now_add=True, readonly=True)
    updatedAt=fields.Date(string="Ultima modificación", auto_now=True, readonly=True)


    @api.model
    def _value_pc(self):
        res = super(ocio__open_ocio__open_events).create()

class ocio__open_ocio__open_images(models.Model):
    _name = 'ocio__open.ocio__open_images'
    _description = 'ocio__open.ocio__open_images'

    
    url = fields.Char(string="Imagen" , required=True)
    render = fields.Binary(string='Image', compute='_renderImageFromUrl', store=True, attachment=False)
    createdAt=fields.Date(string="Fecha de registro", auto_now_add=True)
    updatedAt=fields.Date(string="Ultima modificación", auto_now=True)


    @api.depends('url','render')
    def _renderImageFromUrl(self):
        
        for record in self:
            if record.url:
                record.render = base64.b64encode(requests.get(record.url).content)
                
            