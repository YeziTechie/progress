# Generated by Django 5.0.3 on 2024-04-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_ability'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed_at',
            new_name='done_at',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='is_added',
        ),
        migrations.AddField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
