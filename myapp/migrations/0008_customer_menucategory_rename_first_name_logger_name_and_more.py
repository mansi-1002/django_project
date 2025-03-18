# Generated by Django 5.1.7 on 2025-03-17 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_reservation_alter_logger_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reservation_day', models.CharField(max_length=20)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='logger',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='time',
            new_name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='email',
        ),
        migrations.AddField(
            model_name='reservation',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='category_name', to='myapp.menucategory')),
            ],
        ),
    ]
