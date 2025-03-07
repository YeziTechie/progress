# Generated by Django 5.0.7 on 2024-08-14 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_task_done_at', models.DateTimeField(blank=True, null=True)),
                ('is_achieved', models.BooleanField(default=False)),
                ('achieved_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_hided', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InternalEcology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.TextField(default='Not answered yet.', null=True)),
                ('q2', models.TextField(default='Not answered yet.', null=True)),
                ('q3', models.TextField(default='Not answered yet.', null=True)),
                ('q4', models.TextField(default='Not answered yet.', null=True)),
                ('q5', models.TextField(default='Not answered yet.', null=True)),
                ('q6', models.TextField(default='Not answered yet.', null=True)),
                ('q7', models.TextField(default='Not answered yet.', null=True)),
                ('q8', models.TextField(default='Not answered yet.', null=True)),
                ('outcome', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='internal_ecology', to='outcomes.outcome')),
            ],
        ),
        migrations.CreateModel(
            name='ExternalEcology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.TextField(default='Not answered yet.', null=True)),
                ('q2', models.TextField(default='Not answered yet.', null=True)),
                ('q3', models.TextField(default='Not answered yet.', null=True)),
                ('q4', models.TextField(default='Not answered yet.', null=True)),
                ('outcome', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='external_ecology', to='outcomes.outcome')),
            ],
        ),
        migrations.CreateModel(
            name='OutcomeQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive', models.TextField(default='Not answered yet.', null=True)),
                ('evidence', models.TextField(default='Not answered yet.', null=True)),
                ('specific', models.TextField(default='Not answered yet.', null=True)),
                ('resource', models.TextField(default='Not answered yet.', null=True)),
                ('control', models.TextField(default='Not answered yet.', null=True)),
                ('identity', models.TextField(default='Not answered yet.', null=True)),
                ('relation_with_other_outcomes', models.TextField(default='Not answered yet.', null=True)),
                ('action', models.TextField(default='Not answered yet.', null=True)),
                ('outcome', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='outcome_questions', to='outcomes.outcome')),
            ],
        ),
    ]
