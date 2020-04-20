from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app.models import UserProfileInfo, Topic, Article, AccessRecord 
from app.forms import UserForm, UserProfileInfoForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

def index(request):
    return render(request, 'app/index.html') 

def register(request):
    registred = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user                         # connects profile to user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registred = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registred': registred})

def user_login(request):
    if request.method == 'POST':                                
        username = request.POST.get('username')                 
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)  

        if user:                                               
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('loggedin'))
            else:
                return HttpResponse('Account not active')

        else:
            print('Login failed')
            print('Username: {} and password: {}'.format(username,password))
            return HttpResponse('Invalid login')
    else:
        return render(request, 'app/login.html', {})

@login_required                                      
def you_are_logged_in(request):
    return render(request, 'app/logged_in.html')

@login_required                                       
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:user_login'))