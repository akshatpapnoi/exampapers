# Generated by Django 2.1.4 on 2018-12-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usict', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='image',
            field=models.ImageField(upload_to='media/papers/usict'),
        ),
    ]
