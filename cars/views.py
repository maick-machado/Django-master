from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search)

    return render(
        request=request, 
        template_name='cars.html',
        context={'cars': cars}
        )



def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForm(data=request.POST, files=request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect(to='cars_list')
    else:
        new_car_form = CarForm()
        return render(
            request=request, 
            template_name='new_car.html', 
            context= {'new_car_form': new_car_form}
            )