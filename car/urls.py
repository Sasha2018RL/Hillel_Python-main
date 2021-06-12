from django.urls import path, include
from car.views import car_view, index_view

urlpatterns = [
    path("", index_view),
    path("car/", car_view),
    path("car/<int:obj>", car_view),
]
