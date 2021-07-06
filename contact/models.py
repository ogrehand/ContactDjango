from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    class Meta:
        ordering=['id']

class Contacts(models.Model):
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)
    contactType = models.CharField(max_length=15,blank=True,default='')
    contactId = models.CharField(max_length=30)
