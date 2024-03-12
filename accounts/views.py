from django.shortcuts import render,redirect,resolve_url
# Create your views here.
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse

class Login(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'
    def get_success_url(self):
        messages.success(self.request,'Logged in successfully')
        print ('Login successful')
        return  resolve_url("jobs:list")
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")  # Redirect to the login page upon successful registration
    template_name = 'accounts/signup.html'

class Logout(LogoutView):
  next_page="url 'accounts:login'"

def logout_view(request):

    if(request.method=='POST'):
        logout(request)

    return redirect('accounts:login')
