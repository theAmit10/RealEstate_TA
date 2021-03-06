from django.shortcuts import render, redirect
from django.contrib import messages, auth # auth is used for to give authentication page to the newly created user.
from django.contrib.auth.models import User # this is by default given by django it used for to create user.

from contacts.models import Contact # used for dynamic dashboard

# Create your views here.
def register(request):
    if request.method == 'POST':
        # get the value of the form which use POST methods.
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email'] 
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if password match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The Username is Taken, Try Another One.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The Email is being Used.')
                    return redirect('register')
                else:
                    # looks good if everything is correct than create user.
                    user = User.objects.create_user(username=username, password=password,
                    email=email, first_name=first_name, last_name= last_name )
                    # login after register
                    # auth.login(request, user)
                    # messages.success(request, ' you are noe logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'you are now Registered')
                    return redirect('login')

        else:
            messages.error(request, 'Password Do Not Match.')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password )

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        
       
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are Logged Out ')
    return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
 
    context = {
        'contacts': user_contacts
    }

    return render(request,'accounts/dashboard.html', context)
