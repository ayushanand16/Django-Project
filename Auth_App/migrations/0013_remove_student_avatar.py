# Generated by Django 4.1.3 on 2022-11-10 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_App', '0012_alter_student_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='avatar',
        ),
    ]
