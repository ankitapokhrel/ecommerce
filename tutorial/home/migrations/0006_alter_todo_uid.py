# Generated by Django 4.1.2 on 2022-11-01 11:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('bc11b8cd-a5d1-440c-97bd-446bcbaa04f6'), editable=False, primary_key=True, serialize=False),
        ),
    ]