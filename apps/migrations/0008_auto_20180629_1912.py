# Generated by Django 2.0.6 on 2018-06-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_auto_20180620_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='content',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(max_length=1800),
        ),
        migrations.AlterField(
            model_name='books',
            name='user_created',
            field=models.CharField(max_length=100),
        ),
    ]