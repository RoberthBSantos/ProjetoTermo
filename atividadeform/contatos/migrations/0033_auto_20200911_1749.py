# Generated by Django 3.1 on 2020-09-11 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0032_auto_20200911_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produtos',
            options={'ordering': ('nome',)},
        ),
    ]