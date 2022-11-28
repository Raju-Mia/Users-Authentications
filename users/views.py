from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from . forms import UserCustomRegisterForm

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')

#register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)


#custom register
def customregister(request):
    if request.method == 'POST':
        form = UserCustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserCustomRegisterForm()

    context = {'form': form}
    return render(request, 'user/customregister.html', context)


#login 

def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            usern = form.cleaned_data['username']
            userp = form.cleaned_data['password']
            user = authenticate(username= usern, password=userp)

            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form = AuthenticationForm()
        context= {'form':form}
        return render(request, 'user/login.html', context)



#logout
@login_required(login_url='login')
def logout_form(request):
    logout(request)
    # return redirect('hoem')
    return render(request, 'user/logout.html')



#password chnage
@login_required(login_url='login')
def passwordchange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('login')



        else:
            form = PasswordChangeForm(user= request.user)
            context = {'form':form}
            return render(request, 'user/changepassword.html',context)
    
    else:
        return redirect('login')



#password chnage without old password
@login_required(login_url='login')
def passwordchangeop(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('home')



        else:
            form = SetPasswordForm(user= request.user)
            context = {'form':form}
            return render(request, 'user/changepassword_w_O_P.html',context)
    
    else:
        return redirect('login')