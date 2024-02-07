from django.contrib import admin
from bankapp.models import BankCard

# Register your models here.
@admin.register(BankCard)
class BankCardAdmin(admin.ModelAdmin):
    pass
