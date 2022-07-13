from django.db import models

# Create your models here.
class paymented(models.Model):
    ok = models.CharField(max_length=30 ,blank=True)
    user=models.CharField(max_length=100)
    def __str__(self):
        return str(self.user)