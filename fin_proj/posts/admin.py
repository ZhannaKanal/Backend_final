from django.contrib import admin

# Register your models here.
from .models import Kala
admin.site.register(Kala)

from .models import Service
admin.site.register(Service)

from .models import Second
admin.site.register(Second)

from .models import Price
admin.site.register(Price)

from .models import Pricee
admin.site.register(Pricee)

from .models import Order
admin.site.register(Order)

from .models import Registration
admin.site.register(Registration)

from .models import InfoTravel
admin.site.register(InfoTravel)
