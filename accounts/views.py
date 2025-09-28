from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

# Create your views here.
def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(
        request=request,
        template_name='register.html',
        context={'user_form': user_form}
        )


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm() # colocar uma mensagem que é necessário se cadastrar
    else:
        login_form = AuthenticationForm()
    return render(
        request=request,
        template_name='login.html',
        context={'login_form': login_form}
    )

def logout_view(request):
    logout(request)
    return redirect('cars_list')