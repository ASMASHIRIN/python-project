# Generated by Django 4.1.4 on 2023-08-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0005_alter_registration_dateofbirth'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='dateofbirth',
            field=models.CharField(default='01-01-2000', max_length=200),
        ),
    ]
