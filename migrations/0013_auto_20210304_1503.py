# Generated by Django 3.1.1 on 2021-03-04 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20210221_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_account',
            name='roll',
            field=models.CharField(max_length=30),
        ),
    ]
