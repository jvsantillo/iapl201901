from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    insertion_date = models.DateTimeField('Person insertion date')
    exclusion_date = models.DateTimeField('Person exclusion Date', null=True, blank=True)

class Supplier(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE, 
        primary_key=True,
    )
    insertion_date = models.DateTimeField('Supplier insertion date')
    exclusion_date = models.DateTimeField('Supplier exclusion date', null=True, blank=True)

class Expertise(models.Model):
    field = models.CharField(max_length=200)
    description = models.TextField(max_length=4500)
    insertion_date = models.DateTimeField('Expertise insertion date')
    exclusion_date = models.DateTimeField('Expertise exclusion date', null=True, blank=True) 
    suppliers = models.ManyToManyField(Supplier) 