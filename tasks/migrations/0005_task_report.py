# Generated by Django 5.0.3 on 2024-07-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_remove_task_ability_task_outcome'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='report',
            field=models.TextField(null=True),
        ),
    ]
