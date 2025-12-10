## FIDELIDAD FIDEL FIEL ACTIMEL 🐏

![img](https://i.pinimg.com/originals/97/41/f0/9741f0c6151635b29300e6f7656e1644.gif)

### DESCRIPCIÓN 🐞

>[!NOTE]
> ***EXTENDER EL MÓDULO DE ZODIACO HECHO PASO A PASO ¡SIGUIENDO LA GUÍA! IMPLEMENTANDO LA GESTIÓN DE FIDELIZACIÓN DE CLIENTES***

---

### ARCHIVOS DE CONFIGURACIÓN 🦦

> [!IMPORTANT]
> ***LOS ARCHIVOS DE CONFIGURACIÓN ESTÁN HECHOS SIGUIENDO LA GUÍA, SOLO HUBO QUE IMPLEMENTAR LA PARTE DE FIDELIZACIÓN***

#### MANIFEST.PY

```
'description': """
ESTE MODULO EXTIENDE EL MODELO RES_PARTNER ANADIENDO LOS SIGUIENTES CAMPOS A LOS CONTACTOS:
- FECHA DE NACIMIENTO
- EDAD (CALCULADA AUTOMATICAMENTE)
- SIGNO DEL HOROSCOPO CHINO (CALCULADO AUTOMATICAMENTE)

# SOLO CAMBIÉ LA DESCRIPCIÓN (AÑADÍ LO DE ABAJO)🐟

- CODIGO DE SOCIO           
- NIVEL DE FIDELIDAD        
    """,
```

---

#### VIEWS.XML

> ***SECCIONES AÑADIDAS 🦁***

```
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <data>

    <!-- VISTA FORMULARIO: PESTAÑAS "SIGNO CHINO" Y "MEMBRESIA" -->
    <record id="partner_chinese_stats_form_view" model="ir.ui.view">
        <field name="name">PARTNER.CHINESE.STATS.FORM</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_form"/>
        <field name="arch" type="xml">
            <xpath expr="//notebook" position="inside">
                <page string="SIGNO CHINO">
                    <group>
                        <field name="f_nac" string="FECHA DE NACIMIENTO"/>
                        <field name="edad" string="EDAD"/>
                        <field name="signo_chino" string="SIGNO DEL HOROSCOPO CHINO"/>
                    </group>
                </page>
                <page string="MEMBRESIA">
                    <group>
                        <field name="codigo_socio" string="CODIGO DE SOCIO"/>
                        <field name="nivel_fidelidad" string="NIVEL DE FIDELIDAD"/>
                    </group>
                </page>
            </xpath>
        </field>
    </record>

---------------------------------------------------------------------------------------------------------

    <!-- VISTA LISTA: NIVEL DE FIDELIDAD EN AZUL (decoration-info) -->
    <record id="partner_chinese_stats_list_view" model="ir.ui.view">
        <field name="name">PARTNER.CHINESE.STATS.LIST</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_tree"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='complete_name']" position="after">
                <field name="signo_chino" string="SIGNO CHINO"/>
                <field name="nivel_fidelidad" string="NIVEL DE FIDELIDAD" decoration-info="nivel_fidelidad in ['PREMIUM','GOLD']"/>
            </xpath>
        </field>
    </record>

-----------------------------------------------------------------------------------------------------------

    <!-- VISTA KANBAN: CODIGO DE SOCIO EN NEGRITA - XPATH SIMPLIFICADO -->
    <record id="partner_chinese_stats_kanban_view" model="ir.ui.view">
        <field name="name">PARTNER.CHINESE.STATS.KANBAN</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.res_partner_kanban_view"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='display_name']" position="after">
                <div class="text-muted">
                    <field name="signo_chino" string="SIGNO CHINO"/>
                </div>
                <div class="fw-bold">
                    <field name="codigo_socio" string="CODIGO SOCIO"/>
                </div>
            </xpath>
        </field>
    </record>

  </data>
</odoo>
```

---

#### MODELS.PY

> ***CAMPOS NUEVOS AÑADIDOS ⚖️***

```
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
```

> ***MÉTODOS NUEVOS 🏹***

```
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
```

---
 
### COMPROBACIÓN 🦀

<img width="480" height="420" alt="image" src="https://github.com/user-attachments/assets/5d8e3535-9ef9-420d-9e35-05e22c72252c" />

---

#### VISTA KANBAN 🖤

<img width="480" height="420" alt="image" src="https://github.com/user-attachments/assets/3e9d3a14-c92a-44f6-b7ae-ef0f5e88da6c" />

---

<img width="480" height="420" alt="image" src="https://github.com/user-attachments/assets/f2a03e10-c365-4359-9c0a-848eae04662f" />

---

#### VISTA LISTA 🔵

<img width="480" height="420" alt="image" src="https://github.com/user-attachments/assets/244a5410-8237-42d3-a91d-453c4284ab08" />





