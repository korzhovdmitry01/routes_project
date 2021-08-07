from django.db import models
from cities.models import City
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name of route')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Total travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='route_from_city_set', verbose_name='From')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                related_name='route_to_city_set', verbose_name='To')

    trains = models.ManyToManyField(Train, verbose_name='Trains list')

    def __str__(self):
        return f'Route {self.name} from {self.from_city} to {self.to_city}'

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['travel_times']