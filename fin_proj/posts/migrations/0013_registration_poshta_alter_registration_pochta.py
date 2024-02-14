# Generated by Django 4.0.4 on 2022-05-25 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_registration_pochta_alter_registration_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='poshta',
            field=models.EmailField(blank=True, default='@stu.sdu.edu.kz', max_length=254, verbose_name='Ushinshi Elektrondyk poshta'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='pochta',
            field=models.EmailField(blank=True, default='@stu.sdu.edu.kz', max_length=254, verbose_name='Ekinshi Elektrondyk poshta'),
        ),
    ]
