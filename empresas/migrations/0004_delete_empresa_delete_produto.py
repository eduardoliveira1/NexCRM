# Generated by Django 5.1.6 on 2025-03-28 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_alter_empresa_nome_empresa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
