from django.db import models


#  Many to Many Relationships
class Worker(models.Model):
    name = models.CharField(max_length=255)
    
    
class Machine(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ManyToManyField(
        Worker,
        related_name='Machine'
    )


# #  One to Many Relationship
# class Customer(models.Model):
#     name = models.CharField(max_length=255)
    
    
# class Vehicle(models.Model):
#     name = models.CharField(max_length=255)
#     customer = models.ForeignKey(
#         Customer,
#         on_delete=models.CASCADE,
#         related_name='Vehicle'
#     )


#  One to One relationship

# class Customer(models.Model):
#     name = models.CharField(max_length=255)
    
    
# class Vehicle(models.Model):
#     name = models.CharField(max_length=255)
#     customer = models.OneToOneField(
#         Customer,
#         on_delete=models.CASCADE,
#         related_name='vehicle'
#     )