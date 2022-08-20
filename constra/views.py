from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import (
    Comment,
    Fact,
    News, 
    Project,
)
from django.views.generic import ListView, DetailView

def home_view(request):
    context = {
        'facts': Fact.objects.all(),
        'object_list': Project.objects.all(),
    }
    return render(request, 'constra/home/home.html', context)

def view_404(request):
    return render(request, 'constra/other/404.html',{'msg':'Oops... Page Not Found!'})

def about_view(request):
    context = {
        'facts': Fact.objects.all(),
    }
    return render(request, 'constra/about/about.html', context)

def comment_view(request):
    usn = request.POST['cName']
    nc = User.username
    email = request.POST['cEmail']
    website = request.POST['Website']
    content = request.POST['Content']
    post = news_detail(request)[1]
    cm = Comment.objects.create(name=usn,email=email,about=content,website=website,n_name=nc,post=post)
    cm.save()
    return redirect('./')

def contact_view(request):
    return render(request, 'constra/other/contact.html')

def faq_view(request):
    return render(request, 'constra/other/faq.html')

def login_view(request):
    usn = request.POST['Name']
    passw = request.POST['Passw']
    user = authenticate(username=usn,password=passw)
    if user is not None:
        login(request, user)
        return redirect('home:home')
    else:
        return render(request, 'constra/other/404.html' ,{'msg':'Invalid login. Check credentials!'})

def logout_view(request):
    logout(request)
    return redirect('../')

def reg_view(request):
    usn = request.POST['sName']
    passw = request.POST['sPassw']
    email = request.POST['Email']
    user = User.objects.create_user(username=usn,password=passw,email=email)
    user.save()
    if user is not None:
        login(request, user)
        return redirect('home:home')


def typography_view(request):
    return render(request, 'constra/other/typography.html')

def news_detail(request, id=1):
    object = News.objects.get(id=id)
    if request.POST:
        usn = request.POST['cName']
        email = request.POST['cEmail']
        website = request.POST['Website']
        content = request.POST['Content']
        post = object
        cm = Comment.objects.create(name=usn,email=email,about=content,n_name=request.user,website=website,post=post)
        cm.save()
        return redirect('./')
    comments = Comment.objects.filter(post=object)
    object.comments_all.set(comments)
    context = {
        'object': object,
        'comments': comments,
        'news_list': News.objects.all()
    }
    return render(request, 'constra/news/detail.html', context)


# Custom Views
class CustomList(ListView):
    pass

class CustomDetail(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['news_list'] = News.objects.all()
        except:
            pass
        return context

