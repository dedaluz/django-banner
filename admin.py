from django.contrib import admin
from bohbou.web.models import *
from sorl.thumbnail.admin import AdminImageMixin

class FeaturedSlideOptions(admin.TabularInline):
    fields = ('position', 'status', 'caption', 'description', 'link', 'created',)
    # define the sortable
    sortable_field_name = "position"

class FeaturedAlbumAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('status', 'caption', 'link', 'created')


admin.site.register(Featured, FeaturedAdmin)