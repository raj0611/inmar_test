# Generated by Django 3.2.9 on 2022-04-11 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='Department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='SubCategory',
            new_name='subcategory',
        ),
    ]
