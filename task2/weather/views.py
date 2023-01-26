from rest_framework import generics
from .models import Weather
from .serializers import WeatherSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django.db import models
from .main import add_city, update_check_time


class WeatherFilter(django_filters.FilterSet):
    class Meta:
        model = Weather
        fields = ['city', ]

    # Переопределение filter_queryset
    def filter_queryset(self, queryset):
        for name, value in self.form.cleaned_data.items():
            queryset = self.filters[name].filter(queryset, value.title())
            assert isinstance(
                queryset, models.QuerySet
            ), "Expected '%s.%s' to return a QuerySet, but got a %s instead." % (
                type(self).__name__,
                name,
                type(queryset).__name__,
            )
        """Если в БД имеется нужный город, проверяем дату его обновления.
        Если обновление было позднее чем interval=30 минут, 
        то возвращаем пустой QuerySet, который в следующем условии обновит данные"""
        if len(queryset) == 1:
            time_from_db = queryset[0].time_update
            if not update_check_time(time_from_db, 30):
                queryset = []

        """Если в БД нет нужного города, делаем запрос на openweather
        и записываем новые данные в таблицу, если город есть, то обновляем его данные"""
        if not queryset:
            new_city = self.request.GET.get('city').title()
            new_city_data = add_city(new_city)

            if new_city_data:
                defaults = {
                    'city': new_city,
                    'temperature': new_city_data['temperature'],
                    'atmosphere_pressure': new_city_data['atmosphere_pressure'],
                    'wind_speed': new_city_data['wind_speed']
                }
                Weather.objects.update_or_create(
                    city=new_city,
                    defaults=defaults
                )
                return Weather.objects.filter(city=new_city)
            else:
                return [
                        {
                            "id": None,
                            "city": f'{new_city} - city not found',
                            "temperature": None,
                            "atmosphere_pressure": None,
                            "wind_speed": None,
                            "time_update": None
                        }
                ]
        return queryset


class WeatherAPIView(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WeatherFilter
