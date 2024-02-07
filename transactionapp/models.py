from django.db import models
from bankapp.models import BankCard

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Operation(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    bankcard= models.ForeignKey(BankCard,on_delete=models.PROTECT)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
