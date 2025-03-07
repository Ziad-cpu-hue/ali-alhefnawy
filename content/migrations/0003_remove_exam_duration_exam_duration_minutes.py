# Generated by Django 5.1.6 on 2025-02-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_exam_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='duration',
        ),
        migrations.AddField(
            model_name='exam',
            name='duration_minutes',
            field=models.PositiveIntegerField(default=30, verbose_name='مدة الامتحان بالدقائق'),
        ),
    ]
