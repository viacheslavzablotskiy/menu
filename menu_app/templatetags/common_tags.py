from django import template

from menu_app.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu_app.html', takes_context=True)
def show_menu(context):
    menu_items = MenuItem.objects.filter(level=0)
    return {
        "menu_items": menu_items,
    }
