# Generated by Django 3.1 on 2020-09-10 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0030_listamaterial_projeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listamaterial',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contatos.projeto'),
        ),
    ]
