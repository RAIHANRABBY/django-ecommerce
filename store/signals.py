from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer

@receiver(post_save,sender=User)
def createCustomer(sender,instance,created,**kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save,sender=User)
def updateCustomer(sender,instance,created,**kwargs):
    if not created:
        instance.customer.save()