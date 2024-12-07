from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate

# Create your views here.
def homepage(request):
    return render(request,'adminapp/home.html')

def about(request):
    return render(request,'adminapp/about.html')

def contact(request):
    return render(request,'adminapp/contact.html')

def registercall(request):
    return render(request,'adminapp/register.html')

def registerlogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email

                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/register.html')  #adminapp/UserLoginPageCall.html
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')


def UserLoginPageCall(request):
    return render(request, 'adminapp/login.html')

"""
def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username,password)
        user = authenticate(request, username=username, password=password)


        if user is not None:
            auth.login(request, user)
            if len(username) == 5:
                # Redirect to StudentHomePage
                #messages.success(request, 'Login successful as student!')
                return redirect('userapp:userhomepage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                #messages.success(request, 'Login successful as faculty!')
                return redirect('instructorapp:instructorhomepage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/login.html')
    else:
        return render(request, 'adminapp/login.html')
"""
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if len(username) == 5:
                return redirect('userapp:userhomepage')
            elif len(username) == 4:
                return redirect('instructorapp:instructorhomepage')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/login.html')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'adminapp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('homepage')