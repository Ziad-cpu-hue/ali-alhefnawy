# Generated by Django 5.1.6 on 2025-02-28 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_remove_exam_duration_exam_duration_minutes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='duration',
        ),
    ]
