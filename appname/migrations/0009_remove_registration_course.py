# Generated by Django 4.1.4 on 2023-08-10 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0008_opted_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='course',
        ),
    ]