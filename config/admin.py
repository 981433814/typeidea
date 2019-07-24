from django.contrib import admin
from .models import Link, SideBar
# Register your models here.

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)
@admin.register(SideBar)
class SideBarAdim(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    list_filter = ('title', 'display_type', 'content')
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SideBar, self).save_model(request, obj, form, change)