# Generated by Django 4.1.3 on 2022-11-06 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autoservice", "0006_alter_autoservicesalehistory_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autoservicesalehistory",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 6, 17, 57, 33, 136749)
            ),
        ),
    ]
