# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import frontend

class frontendAdmin(admin.ModelAdmin):
	class Meta:
		model = frontend

admin.site.register(frontend, frontendAdmin)