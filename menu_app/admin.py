from __future__ import absolute_import

from django.contrib import admin
# Register your models here.
from .models import TreeMenu, TreeMenuCategory, MenuItem, Menu
from mptt.admin import MPTTModelAdmin


@admin.register(Menu)
class TreeMenuAdmin(admin.ModelAdmin):
    fields = ['name', 'url', 'position', ]
    list_display = ['__str__', 'name', 'url', 'position', ]


class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(MenuItem, MenuItemMPTTModelAdmin)


@admin.register(TreeMenuCategory)
class TreeMenuCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'verbose_name', ]
    list_display = ['__str__', ]


@admin.register(TreeMenu)
class TreeMenuAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'path', 'parent', ]
    list_display = ['__str__', 'category', 'path', 'parent', ]
