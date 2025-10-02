from django.db import models


class Brand(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):

    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    # quando eu deleto o carro do banco de dados a foto permanece na pasta do projeto
    photos = models.ImageField(
        default="cars/sem_imagem.png",
        upload_to="cars/",
        blank=True,
        null=True,
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "-created_at"
        ]  # o sinal "-" ordena do mais recente para o mais antigo

    def __str__(self):
        return f"Inventory at {self.created_at}: {self.cars_count} cars worth {self.cars_value}"
