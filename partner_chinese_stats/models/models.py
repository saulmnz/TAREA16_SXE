# -*- CODING: UTF-8 -*-

from odoo import models, fields, api
from datetime import date

class PartnerChineseStats(models.Model):
    _inherit = 'res.partner'

    # FECHA DE NACIMIENTO
    f_nac = fields.Date(
        string='FECHA DE NACIMIENTO'
    )

    # EDAD DEL CONTACTO
    edad = fields.Integer(
        string='EDAD',
        compute='_calcular_edad',
        store=True,
        readonly=True
    )

    # SIGNO CHINO DEL CONTACTO
    signo_chino = fields.Char(
        string='SIGNO CHINO',
        compute='_calcular_chinada',
        store=True,
        readonly=True
    )

    # CODIGO DE SOCIO
    codigo_socio = fields.Char(
        string='CODIGO DE SOCIO'
    )

    # NIVEL DE FIDELIDAD
    nivel_fidelidad = fields.Char(
        string='NIVEL DE FIDELIDAD',
        compute='_calcular_nivel_fidelidad',
        store=True,
        readonly=True
    )

    # CALCULAR LA EDAD
    @api.depends('f_nac')
    def _calcular_edad(self):
        for record in self:
            if record.f_nac:
                hoy = date.today()
                record.edad = hoy.year - record.f_nac.year - ((hoy.month, hoy.day) < (record.f_nac.month, record.f_nac.day))
            else:
                record.edad = 0

    # CALCULAR EL SIGNO CHINO
    @api.depends('f_nac')
    def _calcular_chinada(self):
        animales = ['RATA', 'BUEY', 'TIGRE', 'CONEJO', 'DRAGON', 'SERPIENTE',
                    'CABALLO', 'CABRA', 'MONO', 'GALLO', 'PERRO', 'CERDO']

        for record in self:
            if record.f_nac:
                ano = record.f_nac.year
                indice = (ano - 1900) % 12
                record.signo_chino = animales[indice]
            else:
                record.signo_chino = "SIN SIGNO"

    # CALCULAR EL NIVEL DE FIDELIDAD
    @api.depends('codigo_socio')
    def _calcular_nivel_fidelidad(self):
        for record in self:
            if not record.codigo_socio:
                record.nivel_fidelidad = "ESTANDAR"

            elif record.codigo_socio.startswith(('G','g')):
                record.nivel_fidelidad = "GOLD"

            else:
                record.nivel_fidelidad = "PREMIUM"