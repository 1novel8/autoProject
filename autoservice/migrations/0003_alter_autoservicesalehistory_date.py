# Generated by Django 4.1.2 on 2022-10-17 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autoservice", "0002_alter_autoservicesalehistory_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autoservicesalehistory",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 18, 0, 51, 37, 498603)
            ),
        ),
    ]
