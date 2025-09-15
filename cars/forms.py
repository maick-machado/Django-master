from django import forms
from cars.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    year = forms.IntegerField()
    value = forms.FloatField()
    photos = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            year = self.cleaned_data['year'],
            value = self.cleaned_data['value'],
            photos = self.cleaned_data['photos'],
        )
        car.save()
        return car