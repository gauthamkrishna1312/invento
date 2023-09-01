from django.db import models

# Create your models here.
class ticket_info(models.Model):
    IDtkt = models.IntegerField(unique=True)
    status = models.CharField(max_length=50, default='Active')

def __str__(self):
        return self.name