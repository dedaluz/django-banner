from django.contrib import admin
from bohbou.web.models import *
from sorl.thumbnail.admin import AdminImageMixin


class FeaturedAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('status', 'caption', 'link', 'created')

admin.site.register(Featured, FeaturedAdmin)