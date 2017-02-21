from django.contrib import admin

from .models import Item
from .models import Activity

admin.site.register(Item)
admin.site.register(Activity)
