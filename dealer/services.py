from autoservice.serializers import CarSerializer, AutoserviceSerializer


class DealerService:
    car_serializer = CarSerializer
    autoservice_serializer = AutoserviceSerializer

    def get_car_catalog(self, query_set):
        info = list()
        for instance in query_set:
            serializer = self.car_serializer(instance.car)
            cost = instance.cost
            info.append({'car': serializer.data,
                         'cost': cost})
        return info

    def get_sale_history(self, query_set):
        info = list()
        for instance in query_set:
            serializer1 = self.car_serializer(instance.car)
            cost = instance.cost
            date = instance.date
            count = instance.count
            serializer2 = self.autoservice_serializer(instance.autoservice)
            info.append({'date': date,
                         'autoservice': serializer2.data,
                         'car': serializer1.data,
                         'cost': cost,
                         'count': count})
        return info
