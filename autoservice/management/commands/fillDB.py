import random
from string import ascii_letters
from django.core.management import BaseCommand

from autoservice.enums import Brands, BodyTypes, FuelTypes
from autoservice.models import Car, Autoservice
from customer.models import Customer
from dealer.models import Dealer


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(10):
            dealer = self.create_dealer()
            for j in range(20):
                dealer.car_catalog.add(self.create_car())
            self.create_autoservice()
            self.create_customer()

    def create_car(self):
        car = Car.objects.create(
            brand=random.choice(list(Brands)).value,
            body_type=random.choice(list(BodyTypes)).value,
            issue_year=random.randint(1990, 2022),
            model_of_car=''.join(random.choice(ascii_letters) for i in range(4)),
            fuel_type=random.choice(list(FuelTypes)).value,
            mileage=random.randint(0, 200000),
        )
        return car

    def create_autoservice(self):
        Autoservice.objects.create(
            name=''.join(random.choice(ascii_letters) for i in range(10)),
            feature_preference=self.generate_preference(),
            balance=0
        )

    def generate_preference(self):
        preference = {
            "body_type": random.choice(list(BodyTypes)).value,
            "fuel_type": random.choice(list(FuelTypes)).value,
            "brand": random.choice(list(Brands)).value
        }
        return preference

    def create_customer(self):
        Customer.objects.create(
            name=''.join(random.choice(ascii_letters) for i in range(8)),
            surname=''.join(random.choice(ascii_letters) for i in range(12))
        )

    def create_dealer(self):
        dealer = Dealer.objects.create(
            name=''.join(random.choice(ascii_letters) for i in range(12)),
            year_of_creation=random.randint(1990, 2022)
        )
        return dealer
