# Generated by Django 2.0.6 on 2018-06-30 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0014_auto_20180629_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='user_created',
        ),
    ]
