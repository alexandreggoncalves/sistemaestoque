# Generated by Django 5.1.1 on 2024-10-28 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('idFornecedor', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('idCidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cidade.cidade')),
            ],
            options={
                'ordering': ['-nome'],
            },
        ),
    ]
