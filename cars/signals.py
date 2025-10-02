from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory


# @receiver(pre_save, sender="cars.Car")
# def car_pre_save(sender, instance, **kwargs):
#     # possivel usar para enviar email assim que for cadastrado ou deletado
#     print(f"Pre-save signal triggered for Car: {instance}")
def car_invetory_update():
    cars_count = Car.objects.all().count()
    # cars_value = sum(car.value for car in Car.objects.all() if car.value)
    cars_value = Car.objects.aggregate(total_valeu=Sum("value"))[
        "total_valeu"
    ]  # como retorna um dicionário, usa-se o ["total_value"] para acessar somente o valor
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


@receiver(pre_save, sender="cars.Car")
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = "Sem descrição"


@receiver(post_save, sender="cars.Car")
def car_post_save(sender, instance, **kwargs):
    # if created: da para adicionar o if created e adicionar o created nos parametros da função para diferenciar se é criação ou atualização
    car_invetory_update()


# @receiver(pre_delete, sender="cars.Car")
# def car_pre_delete(sender, instance, **kwargs):
#     print(f"Pre-delete signal triggered for Car: {instance}")


@receiver(post_delete, sender="cars.Car")
def car_post_delete(sender, instance, **kwargs):
    car_invetory_update()
