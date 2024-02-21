from django.db import models

# Create your models here.

class BankCard(models.Model):
    name= models.CharField(max_length=255)
    balance= models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,blank=True
    )
    img = models.ImageField(blank=True,null=True)

    def __str__(self):
        return f'{self.name}-{self.balance}'

    def get_absolute_url(self):
        return f'/card/{self.id}'
