# Generated by Django 2.0.6 on 2018-06-20 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20180618_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='user_created',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
