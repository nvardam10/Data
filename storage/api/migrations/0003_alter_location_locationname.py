# Generated by Django 4.2.4 on 2023-08-10 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_item_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='locationName',
            field=models.CharField(max_length=100),
        ),
    ]
