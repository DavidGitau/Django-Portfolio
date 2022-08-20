from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import EditForm, ResetForm
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm



def login_view(request):
    username = request.POST['loginNam']
    password = request.POST['loginPassword']
    user = authenticate(request, username=username, password=password)
    # user = User(username=username)
    # user.is_superuser = True
    # user.is_staff = True
    if user is not None:
        login(request, user)
        # return HttpResponse(messages.success(request, f"logged in successfully!"))
        return redirect('../../')
    else:
        raise Http404('Login unsuccessful!')

def create_view(request):
    fname = request.POST['fName']
    lname = request.POST['lName']
    email = request.POST['eMail']
    username = request.POST['signupName']
    password = request.POST['signupPassword']
    # typ = request.POST['tYpe']
    user = User.objects.create_user(first_name=fname, last_name=lname, email=email, password=password, username=username)
    user.save()
    usr = authenticate(username=username, password=password)
    if usr is not None:
        login(request, user)
        return redirect('../profile/')
    else:
        raise Http404('Reg unsuccessful!')

def logout_view(request):
    logout(request)
    return redirect('user:home')

def profile_view(request):
    return render(request,'profile/profile.html')

def profile_edit(request):
    form = EditForm
    return render(request, 'profile/edit.html', {'form':form})

class EditUser(UpdateView):
    model = User
    form_class = EditForm
    template_name = 'profile/edit.html'
    success_url = '../'

class ResetPass(UpdateView):
    model = User
    user = User.objects.get(id=1)
    form_class = ResetForm(user)
    template_name = 'profile/edit.html'
    success_url = '../'