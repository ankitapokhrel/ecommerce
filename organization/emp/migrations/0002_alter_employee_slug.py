# Generated by Django 4.1.4 on 2022-12-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
