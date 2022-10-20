# Generated by Django 4.1.2 on 2022-10-17 21:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autoservice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_of_creation", models.DateTimeField(auto_now_add=True)),
                ("date_of_last_modification", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=30)),
                ("feature_preference", models.JSONField()),
                ("balance", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_of_creation", models.DateTimeField(auto_now_add=True)),
                ("date_of_last_modification", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "brand",
                    models.CharField(
                        choices=[
                            ("AUDI", "Audi"),
                            ("ALFA_ROMEO", "Alfa Romeo"),
                            ("BENTLEY", "Bentley"),
                            ("BMW", "BMW"),
                            ("BUGATTI", "Bugatti"),
                            ("CADILLAC", "Cadillac"),
                            ("CHEVROLET", "Chevrolet"),
                            ("CITROEN", "Citroen"),
                            ("DODGE", "Dodge"),
                            ("FERRARI", "Ferrari"),
                            ("FORD", "Ford"),
                            ("LEXUS", "Lexus"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "body_type",
                    models.CharField(
                        choices=[
                            ("sedan", "SEDAN"),
                            ("coupe", "COUPE"),
                            ("sport car", "SPORT_CAR"),
                            ("station vagon", "STATION_VAGON"),
                            ("hatchback", "HATCHBACK"),
                            ("convertible", "CONVERTIBLE"),
                            ("minivan", "MINIVAN"),
                            ("pickup truck", "PICKUP_TRACK"),
                            ("crossover", "CROSSOVER"),
                        ],
                        max_length=30,
                    ),
                ),
                ("issue_year", models.IntegerField(default=0)),
                ("model_of_car", models.CharField(max_length=30)),
                (
                    "fuel_type",
                    models.CharField(
                        choices=[
                            ("petrol", "petrol"),
                            ("disel", "disel"),
                            ("CNG", "CNG"),
                            ("bio disel", "bio_disel"),
                            ("electric", "electric"),
                        ],
                        max_length=30,
                    ),
                ),
                ("mileage", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AutoserviceSaleHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cost", models.IntegerField(default=0)),
                (
                    "date",
                    models.DateTimeField(
                        default=datetime.datetime(2022, 10, 18, 0, 50, 44, 313855)
                    ),
                ),
                (
                    "autoservice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="autoservice.autoservice",
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="autoservice.car",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AutoserviceCarCatalog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cost", models.IntegerField(default=0)),
                ("count", models.IntegerField(default=0)),
                (
                    "autoservice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="autoservice.autoservice",
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="autoservice_car",
                        to="autoservice.car",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="autoservice",
            name="car_catalog",
            field=models.ManyToManyField(
                through="autoservice.AutoserviceCarCatalog", to="autoservice.car"
            ),
        ),
        migrations.AddField(
            model_name="autoservice",
            name="sale_history",
            field=models.ManyToManyField(
                through="autoservice.AutoserviceSaleHistory", to="customer.customer"
            ),
        ),
    ]
