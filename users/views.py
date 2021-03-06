from django.shortcuts import render, redirect
#django can generate its own html user creation form which handles all the validations(regex etc.)
from django.contrib import messages #create flash messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #yeah simple as that. the user created and saved in the database
            #the password is also hashed in before commiting to the database
            username = form.cleaned_data.get('username') #cleaned_data is a dictionary
            # messages.success
            # messages.error
            # messages.warning
            # messages.info
            # messages.DEBUG
            messages.success(request, f'Account created for {username}!')
            #no need to the send the messages argument to the redirect method
            #it's an attribute which is part of the request
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES,
                                    instance = request.user.profile
                                    )
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)