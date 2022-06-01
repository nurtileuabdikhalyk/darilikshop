from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(DariShopter)
class DariShopterAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'count', 'created_at', )
    list_display_links = ('name', 'type',)
    prepopulated_fields = {'slug': ('name',), }
    list_filter = ('name', 'type', 'created_at')
    search_fields = ('name', 'type', 'description', 'scientists')

    def preview(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' style='width:100px;height:60px;'>")


@admin.register(Scientists)
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'lauazym',)
    list_display_links = ('name', 'surname',)
    prepopulated_fields = {'slug': ('name', 'surname'), }
    list_filter = ('name', 'surname', 'lauazym')
    search_fields = ('name', 'surname', 'lauazym',)




@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'created_at',)
    list_display_links = ('name', 'director',)
    prepopulated_fields = {'slug': ('name',), }
    list_filter = ('name', 'director', 'created_at')
    search_fields = ('name', 'director',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'tau_aty',)
    list_display_links = ('name', 'district', 'tau_aty')
    prepopulated_fields = {'slug': ('name', 'district'), }
    list_filter = ('name', 'district', 'tau_aty')
    search_fields = ('name', 'district',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'publish',)
    list_display_links = ('name', 'email',)
    list_filter = ('name', 'email', 'publish')
    search_fields = ('name', 'title', 'email', 'text')


admin.site.register(Tur)
