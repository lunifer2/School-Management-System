# Generated by Django 4.1.7 on 2023-04-05 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0003_alter_student_father_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course_name',
            new_name='course_id',
        ),
    ]
