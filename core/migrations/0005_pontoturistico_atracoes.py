# Generated by Django 4.2.1 on 2023-05-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_alter_atracao_options'),
        ('core', '0004_alter_pontoturistico_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.atracao'),
        ),
    ]
