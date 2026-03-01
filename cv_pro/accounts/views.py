from django.shortcuts import render # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views import generic # type: ignore

   

def home(request):
    return render(request, 'home.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
