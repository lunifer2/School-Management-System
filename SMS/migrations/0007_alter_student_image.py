# Generated by Django 4.1.7 on 2023-04-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0006_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.FileField(blank=True, upload_to='../Images/'),
        ),
    ]
