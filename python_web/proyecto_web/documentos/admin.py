# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#IMPORTAR EL MODELO
from documentos.models import Documento

# Register your models here.
#CREAR CLASE DE admin.ModelAdmin

class DocumentoAdmin(admin.ModelAdmin):
	model = Documento
	list_display = ['nombre', 'fecha']


#Registrar ModelAdmin para cada modelo
admin.site.register(Documento,DocumentoAdmin)
