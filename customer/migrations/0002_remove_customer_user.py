# Generated by Django 4.1.3 on 2022-11-06 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="user",
        ),
    ]
