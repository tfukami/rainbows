from django.contrib import admin
from .models import Prof
from .models import Children
from .models import Partner
from .models import Schedules
from .models import Friends

# Register your models here.
admin.site.register(Prof)
admin.site.register(Children)
admin.site.register(Partner)
admin.site.register(Schedules)
admin.site.register(Friends)
