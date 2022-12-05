# Generated by Django 4.1.2 on 2022-11-01 10:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('5d0f6521-321a-4ed3-b1cb-ed4d5a9c9269'), editable=False, primary_key=True, serialize=False),
        ),
    ]
