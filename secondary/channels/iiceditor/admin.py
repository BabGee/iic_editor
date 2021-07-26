from django.contrib import admin

from django.conf.urls import include, url

from django.db import models

from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.db.models import Q

from primary.core.administration.models import Role
from secondary.channels.iic.editor.administration.forms import RoleForm

from primary.core.upc.models import (
    Gateway,
    AccessLevelStatus
)

# IIC editor model
class IICEditor(models.Model):
 
	class Meta:
		verbose_name_plural = 'IIC Editor'
		app_label = 'iiceditor'
        
@staff_member_required
def gateway_list(request):
   #filter gateways
	gateways = Gateway.objects.all()
	return render(request, 'iiceditor/gateway/list.html', {'gateways':gateways})


@staff_member_required
def gateway_detail(request, gateway_pk):
    # filter gateway
    gateway = Gateway.objects.get(pk=gateway_pk)

    return render(request, "iiceditor/gateway/detail.html", {'gateway': gateway})


class IICEditorAdmin(admin.ModelAdmin):
	model = IICEditor
 
	def get_urls(self):
		view_name = f'{self.model._meta.app_label}_{self.model._meta.model_name}_changelist'
		return [
			url(r'^$', gateway_list, name=view_name),
            url(r'^(?P<gateway_pk>\d+)/', include([
                url(r'^$', gateway_detail),
                url(r'^(?P<service_name>[\w\ ]+)/', include('secondary.channels.iiceditor.bridge.urls')),
                ]
                )),
		]

admin.site.register(IICEditor, IICEditorAdmin)