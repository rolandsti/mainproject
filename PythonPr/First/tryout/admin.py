from django.contrib import admin

# Register your models here.
from .models import content
admin.site.register (content)

from .models import numbers
admin.site.register (numbers)