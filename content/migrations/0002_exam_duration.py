# Generated by Django 5.1.6 on 2025-02-28 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='duration',
            field=models.PositiveIntegerField(default=1800, verbose_name='مدة الامتحان بالثواني'),
        ),
    ]
