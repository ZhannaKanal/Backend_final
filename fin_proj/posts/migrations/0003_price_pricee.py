# Generated by Django 4.0.4 on 2022-05-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_second_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kala', models.CharField(default='', max_length=255, verbose_name='Kala')),
                ('hotel', models.CharField(max_length=255, verbose_name='Hotel')),
                ('transport', models.TextField(blank=True, default='', verbose_name='Transport')),
                ('sight', models.CharField(max_length=255, verbose_name='Sight')),
                ('meal', models.TextField(blank=True, default='', verbose_name='Meal')),
                ('price', models.IntegerField(default=20000, verbose_name='Bagga')),
            ],
        ),
        migrations.CreateModel(
            name='Pricee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kala', models.CharField(default='', max_length=255, verbose_name='Kala')),
                ('hotel', models.CharField(max_length=255, verbose_name='Hotel')),
                ('transport', models.TextField(blank=True, default='', verbose_name='Transport')),
                ('sight', models.CharField(max_length=255, verbose_name='Sight')),
                ('meal', models.TextField(blank=True, default='', verbose_name='Meal')),
                ('price', models.IntegerField(default=20000, verbose_name='Bagga')),
            ],
        ),
    ]
