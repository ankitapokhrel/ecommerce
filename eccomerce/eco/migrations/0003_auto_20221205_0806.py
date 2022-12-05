# Generated by Django 3.1.7 on 2022-12-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0002_alter_item_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='c_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='u_name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
