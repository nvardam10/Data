# Generated by Django 4.2.4 on 2023-08-12 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='UserID',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
