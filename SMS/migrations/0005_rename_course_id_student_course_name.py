# Generated by Django 4.1.7 on 2023-04-05 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0004_rename_course_name_student_course_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course_id',
            new_name='course_name',
        ),
    ]