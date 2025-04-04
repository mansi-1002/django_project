# Generated by Django 5.1.7 on 2025-03-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_customer_menuitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('time_log', models.TimeField(help_text='Enter the exact time')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='category_id',
        ),
        migrations.DeleteModel(
            name='Menuitems',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='MenuCategory',
        ),
    ]
