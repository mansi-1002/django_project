# Generated by Django 5.1.7 on 2025-03-17 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20250317_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='menu_item',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='category_id',
        ),
    ]
