from django.contrib import admin
from transactionapp.models import Operation,Category

# Register your models here.
@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
