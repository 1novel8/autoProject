import enum


class Brands(enum.Enum):
    AUDI = 'Audi'
    ALFA_ROMEO = 'Alfa Romeo'
    BENTLEY = 'Bentley'
    BMW = 'BMW'
    BUGATTI = 'Bugatti'
    CADILLAC = 'Cadillac'
    CHEVROLET = 'Chevrolet'
    CITROEN = 'Citroen'
    DODGE = 'Dodge'
    FERRARI = 'Ferrari'
    FORD = 'Ford'
    LEXUS = 'Lexus'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class BodyTypes(enum.Enum):
    SEDAN = 'sedan'
    COUPE = 'coupe'
    SPORT_CAR = 'sport car'
    STATION_VAGON = 'station vagon'
    HATCHBACK = 'hatchback'
    CONVERTIBLE = 'convertible'
    MINIVAN = 'minivan'
    PICKUP_TRACK = 'pickup truck'
    CROSSOVER = 'crossover'

    @classmethod
    def choices(cls):
        return tuple((item.value, item.name) for item in cls)


class FuelTypes(enum.Enum):
    petrol = 'petrol'
    disel = 'disel'
    CNG = 'CNG'
    bio_disel = 'bio disel'
    electric = 'electric'

    @classmethod
    def choices(cls):
        return tuple((item.value, item.name) for item in cls)
