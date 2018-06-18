# Generated by Django 2.0.6 on 2018-06-17 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='book',
        ),
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
    ]