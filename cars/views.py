from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.views import View
from django.views.generic import ListView


class CarsListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")

        if search:
            return cars.filter(
                model__icontains=search
            )  # ou cars = cars.filter(model__icontains=search)
        return cars


class NewCarView(View):
    def get(self, request):
        new_car_form = CarForm()
        return render(
            request=request,
            template_name="new_car.html",
            context={"new_car_form": new_car_form},
        )  # após adicionado o novo carro, criar uma mensagem de sucesso

    def post(self, request):
        new_car_form = CarForm(data=request.POST, files=request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect(
                to="cars_list"
            )  # após erro de algo errado, informar ao usuário
        return render(
            request=request,
            template_name="new_car.html",
            context={"new_car_form": new_car_form},
        )
