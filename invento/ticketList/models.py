from django.db import models

# Create your models here.
class ticket_info(models.Model):
    IDtkt = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Active')
    date = models.DateField()

def __str__(self):
        return self.name
