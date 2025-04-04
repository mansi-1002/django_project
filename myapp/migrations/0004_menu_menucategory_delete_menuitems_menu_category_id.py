# Generated by Django 5.1.7 on 2025-03-17 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_name_menuitems_item_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Menuitems',
        ),
        migrations.AddField(
            model_name='menu',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='category_name', to='myapp.menucategory'),
        ),
    ]
