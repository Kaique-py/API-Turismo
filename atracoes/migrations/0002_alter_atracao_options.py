# Generated by Django 4.2.1 on 2023-05-23 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atracao',
            options={'ordering': ('nome',), 'verbose_name_plural': 'Atrações'},
        ),
    ]
