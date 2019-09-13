from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
#django can generate its own html user creation form which handles all the validations(regex etc.)
from django.contrib import messages #create flash messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #yeah simple as that. the user created and saved in the database
            username = form.cleaned_data.get('username') #cleaned_data is a dictionary
            # messages.success
            # messages.error
            # messages.warning
            # messages.info
            # messages.DEBUG
            message = messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
