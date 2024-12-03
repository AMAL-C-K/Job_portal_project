from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.template.defaultfilters import length
from django.contrib.auth import authenticate, login
from accounts_app.models import Profile
from django.contrib.auth.decorators import login_required
import re





def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']


        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
        elif password != confirm_password:
            messages.error(request, 'password not matching')
        elif not re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$', password):
            messages.error(request, 'password contains atleast one (0-9),(a-z),(A-Z) special characters ')
        
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)    
            user.save()
            return redirect('signin')
    return render(request, 'signup.html')    


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('joblist')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('/')
    return render(request, 'index.html')    

def signout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='/') 
def profile(request):
    profile = None
    try: 
        profile = Profile.objects.get(user=request.user)

    except Profile.DoesNotExist:
        if request.method == 'POST':
            name = request.POST['name']
            age = request.POST['age']
            education = request.POST['education']
            technical_skills= request.POST['technical_skills']
            softskills = request.POST['softskills']
            profile = Profile.objects.create(user=request.user, name=name, age=age,education=education,
                                              techical_skills=technical_skills, softskills=softskills)
            profile.save()
          
    return render(request, 'home.html', {'profile':profile})  
        
@login_required(login_url='/')        
def update_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id, user=request.user)
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        education = request.POST['education']
        technical_skills = request.POST['technical_skills']
        softskills = request.POST['softskills']
        profile = Profile.objects.get(id=profile_id, user=request.user) 

        profile.name = name
        profile.age = age
        profile.education = education
        profile.techical_skills = technical_skills
        profile.softskills = softskills
        profile.save()
        return redirect('profile')
    return render(request, 'update.html', {'profile':profile})    

@login_required(login_url='/')
def delete_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id, user=request.user)
    profile.delete()
    return redirect('profile')