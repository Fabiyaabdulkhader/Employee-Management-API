from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Employee

@receiver(pre_save,sender=Employee)
def convert_name_uppercase(sender,instance,**kwargs):
    instance.name=instance.name.upper()
