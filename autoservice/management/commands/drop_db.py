from django.core.management import BaseCommand

from autoservice.models import Car, Autoservice, AutoserviceCarCatalog, AutoserviceSaleHistory
from customer.models import Customer
from dealer.models import Dealer, DealerCarCatalog, DealerSaleHistory


class Command(BaseCommand):
    def handle(self, car=None, *args, **kwargs):
        AutoserviceCarCatalog.objects.all().delete()
        AutoserviceSaleHistory.objects.all().delete()
        DealerSaleHistory.objects.all().delete()
        DealerCarCatalog.objects.all().delete()

        Autoservice.objects.all().delete()
        Customer.objects.all().delete()
        Dealer.objects.all().delete()
        Car.objects.all().delete()
