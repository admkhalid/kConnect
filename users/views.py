from django.shortcuts import render, redirect
#django can generate its own html user creation form which handles all the validations(regex etc.)
from django.contrib import messages #create flash messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #yeah simple as that. the user created and saved in the database
            username = form.cleaned_data.get('username') #cleaned_data is a dictionary
            # messages.success
            # messages.error
            # messages.warning
            # messages.info
            # messages.DEBUG
            message = messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')