# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import View

from django.shortcuts import render
from documentos.models import Documento

# Create your views here.
class Documentos(View):
	def get(self, request, *arg, **kwargs):

		docs = Documento.objects.all()
		context ={
		    'docs': docs,
		    'encabezado': 'Mis documentos'
		}
		return render(
			request,
			'documento.html',
			context
		)
		
