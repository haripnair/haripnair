# Generated by Django 3.1.4 on 2021-02-19 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210219_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_model',
            old_name='photo',
            new_name='Photo',
        ),
    ]
