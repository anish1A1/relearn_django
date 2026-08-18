from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_POST

from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()  #saves the new user to the database
            login(request, user)
            # Automatically logs the user in after registration
            return redirect('home')
            
    else:
        # if user is not trying to log in then 
        # display the forms fields to template.
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username = email, password = password)
        
        if user is not None:
            login(request, user)
        else:
            messages.error(request, "Invalid email or password!")
    return render(request, 'login.html')

@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')

