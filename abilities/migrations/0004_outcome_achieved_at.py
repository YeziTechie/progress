# Generated by Django 5.0.7 on 2024-08-10 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abilities', '0003_outcome_is_achieved_outcome_is_hided'),
    ]

    operations = [
        migrations.AddField(
            model_name='outcome',
            name='achieved_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
