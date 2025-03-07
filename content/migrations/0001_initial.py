# Generated by Django 5.1.6 on 2025-02-25 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان الكورس')),
                ('description', models.TextField(verbose_name='الوصف')),
                ('image', models.ImageField(upload_to='course_images/', verbose_name='الصورة')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='السعر')),
                ('grade', models.CharField(choices=[('first', 'الصف الأول'), ('second', 'الصف الثاني'), ('third', 'الصف الثالث')], default='first', max_length=10, verbose_name='الصف الدراسي')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ آخر تحديث')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان الامتحان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الوصف')),
                ('grade', models.CharField(blank=True, choices=[('first', 'الصف الأول'), ('second', 'الصف الثاني'), ('third', 'الصف الثالث')], max_length=10, null=True, verbose_name='الصف الدراسي')),
                ('week', models.CharField(blank=True, choices=[('week1', 'الأسبوع الأول'), ('week2', 'الأسبوع الثاني'), ('week3', 'الأسبوع الثالث'), ('week4', 'الأسبوع الرابع')], max_length=10, null=True, verbose_name='الأسبوع')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الإضافة')),
                ('total_mcq_score', models.PositiveIntegerField(default=0, verbose_name='المجموع الكلي للأسئلة الاختيارية')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.course', verbose_name='كورس الشهر')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان المحاضرة')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الوصف')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='ملف الفيديو')),
                ('grade', models.CharField(blank=True, choices=[('first', 'الصف الأول'), ('second', 'الصف الثاني'), ('third', 'الصف الثالث')], max_length=10, null=True, verbose_name='الصف الدراسي')),
                ('week', models.CharField(blank=True, choices=[('week1', 'الأسبوع الأول'), ('week2', 'الأسبوع الثاني'), ('week3', 'الأسبوع الثالث'), ('week4', 'الأسبوع الرابع')], max_length=10, null=True, verbose_name='الأسبوع')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الإضافة')),
                ('duration', models.PositiveIntegerField(default=0, verbose_name='مدة المحاضرة (بالدقائق)')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.course', verbose_name='كورس الشهر')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(blank=True, choices=[('mcq', 'اختياري'), ('essay', 'مقالي')], max_length=10, null=True, verbose_name='نوع السؤال')),
                ('text', models.TextField(blank=True, null=True, verbose_name='نص السؤال')),
                ('image', models.ImageField(blank=True, null=True, upload_to='questions/', verbose_name='صورة السؤال')),
                ('score', models.FloatField(default=0, editable=False, verbose_name='درجة السؤال')),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='content.exam', verbose_name='الامتحان')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='نص الإجابة')),
                ('is_correct', models.BooleanField(default=False, verbose_name='إجابة صحيحة')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='content.question', verbose_name='السؤال')),
            ],
        ),
    ]
