from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    vin_number = models.CharField(max_length=100)
    car_model = models.ForeignKey("car.CarModel", on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=50, default='white')
    product_date = models.DateField()
    car_type = models.ForeignKey("car.CarType", on_delete=models.SET_NULL, null=True)

    def company(self):
        return self.car_model.company

    def __str__(self):
        return f"Машина {self.name} ({self.car_type})"


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey("car.Company", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Производители"
        verbose_name = 'Производитель'


class CarType(models.Model):
    car_type = models.CharField(max_length=50)

    def __str__(self):
        return self.car_type

    class Meta:
        verbose_name_plural = 'Типы машин'
        verbose_name = 'Тип машины'