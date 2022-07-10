from django.db import models
from users.models import CustomUser
from random import randrange
# Create your models here.

class code(models.Model):
    number = models.CharField(max_length=5 ,blank=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)
        
    def save(self,*args,**kwargs):
        code_str=str(randrange(10000,99999))
        self.number = code_str
        super().save(*args,**kwargs)

