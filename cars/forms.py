from django import forms
from cars.models import Car

# class CarFormsss(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     year = forms.IntegerField()
#     value = forms.FloatField()
#     photos = forms.ImageField()

#     def save(self):
#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             year = self.cleaned_data['year'],
#             value = self.cleaned_data['value'],
#             photos = self.cleaned_data['photos'],
#         )
#         car.save()
#         return car
    
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_year(self) : 
        year = self.cleaned_data.get('year')
        if year < 1900: 
            self.add_error('year', 'carros muito antigos não são aceitos')
        return year