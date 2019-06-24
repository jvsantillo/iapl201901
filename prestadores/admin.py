from django.contrib import admin
from .models import Person
from .models import Supplier
from .models import Expertise

# Register your models here.
admin.site.register(Person)
admin.site.register(Expertise)
admin.site.register(Supplier)