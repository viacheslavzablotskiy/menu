# Generated by Django 4.1.4 on 2023-05-06 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_menu_menuitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('position',), 'verbose_name': 'Пункт меню', 'verbose_name_plural': 'Пункт меню'},
        ),
    ]
