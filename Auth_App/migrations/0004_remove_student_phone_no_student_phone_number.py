# Generated by Django 4.1 on 2022-11-04 19:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_App', '0003_hostel_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='+91', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
            preserve_default=False,
        ),
    ]
