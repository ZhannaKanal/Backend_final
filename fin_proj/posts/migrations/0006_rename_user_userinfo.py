# Generated by Django 4.0.4 on 2022-05-22 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Userinfo',
        ),
    ]
