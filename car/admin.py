from django.contrib import admin
from .models import Car, CarModel, Company, CarType


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "vin_number",
        "color",
        "car_model",
        "company",
        "car_type",
        "product_date"
    ]
    fieldsets = (
        (None, {
            'fields': (
                ("name", "vin_number", "color"),
            )
        }),
        ('Advanced options', {
            'fields': ("car_model", "car_type", "company", 'product_date'),
        }),
    )
    readonly_fields = [
        "company"
    ]


class CarInline(admin.StackedInline):
    model = Car


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]
    inlines = [
        CarInline,
    ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = [
        'car_type'
    ]
