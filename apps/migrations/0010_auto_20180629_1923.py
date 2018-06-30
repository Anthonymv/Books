# Generated by Django 2.0.6 on 2018-06-29 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_auto_20180629_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='content',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='books',
            name='user_created',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]