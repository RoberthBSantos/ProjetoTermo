# Generated by Django 2.1.3 on 2021-03-21 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0062_auto_20210305_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='sub_item',
        ),
        migrations.AddField(
            model_name='subitem',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produto', to='contatos.Produtos'),
        ),
        migrations.AddField(
            model_name='subitem',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contatos.Produtos'),
        ),
    ]