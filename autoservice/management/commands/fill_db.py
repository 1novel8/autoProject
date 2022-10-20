import random
from string import ascii_letters
from django.core.management import BaseCommand

from autoservice.enums import Brands, BodyTypes, FuelTypes
from autoservice.models import Car, Autoservice
from customer.models import Customer
from dealer.models import Dealer, DealerCarCatalog


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        dealer_list = list()
        car_list = list()
        autoservice_list = list()
        for i in range(50):
            car_list.append(self.create_car())
        for i in range(10):
            dealer_list.append(self.create_dealer())
        for i in range(20):
            autoservice_list.append(self.create_autoservice())
        for car in car_list:
            for dealer in dealer_list:
                if random.randint(0, 2) == 1:
                    dealer_catalog = DealerCarCatalog(car=car,
                                                      dealer=dealer,
                                                      cost=random.randint(10000, 30000) / random.randint(1, 3))
                    dealer_catalog.save()

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
        autoservice = Autoservice.objects.create(
            name=''.join(random.choice(ascii_letters) for i in range(10)),
            feature_preference=self.generate_preference(),
            balance=0
        )
        return autoservice

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
