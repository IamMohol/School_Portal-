from django.contrib import admin
from .models import Finance, FinanceHistory

# Register your models here.
admin.site.register(Finance)
admin.site.register(FinanceHistory)