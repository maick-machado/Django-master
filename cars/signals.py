from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from cars.models import Car


@receiver(pre_save, sender="cars.Car")
def car_pre_save(sender, instance, **kwargs):
    # possivel usar para enviar email assim que for cadastrado ou deletado
    print(f"Pre-save signal triggered for Car: {instance}")


@receiver(post_save, sender="cars.Car")
def car_post_save(sender, instance, **kwargs):
    print(f"Post-save signal triggered for Car: {instance}")


@receiver(pre_delete, sender="cars.Car")
def car_pre_delete(sender, instance, **kwargs):
    print(f"Pre-delete signal triggered for Car: {instance}")


@receiver(post_delete, sender="cars.Car")
def car_post_delete(sender, instance, **kwargs):
    print(f"Post-delete signal triggered for Car: {instance}")
