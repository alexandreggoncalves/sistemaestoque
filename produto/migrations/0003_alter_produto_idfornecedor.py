# Generated by Django 5.1.1 on 2024-10-28 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0001_initial'),
        ('produto', '0002_alter_produto_idcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='idFornecedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fornecedor.fornecedor'),
        ),
    ]