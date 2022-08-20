from django import views
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from datetime import date
from django.db.models import Q
from django.views.generic import (
    ListView, 
    DetailView
)
from .models import (
    About,
    Blog, 
    Course,  
    Event,
    FunFact, 
    Notice, 
    Research, 
    Scholarship,
    Teacher 
)


"""------------------------------------------------------------

                    FUNCTION BASED VIEWS
                    
------------------------------------------------------------"""

def base_view(request):
    title = About.objects.get(id=2)
    return title

def home_view(request):
    course_list = Course.objects.filter(id__lt=7)
    course_detail = get_object_or_404(course_list, pk=1)
    teacher_list = Teacher.objects.filter(id__lt=4)
    teacher_detail = get_object_or_404(teacher_list, pk=1)
    blog_reccommend = Blog.objects.filter(post_date__lt=date(2022,4,21))
    context = {
        'course_list': course_list,
        'course_detail': course_detail,
        'teacher_list': teacher_list,
        'teacher_detail': teacher_detail,
        'blog_reccommend': blog_reccommend,
    }
    return render(request, 'core/home.html', context)

def about_view(request):
    about = About.objects.all()
    fun_facts = FunFact.objects.all()
    about = get_object_or_404(about, pk=1)
    teacher_list = Teacher.objects.filter(id__lt=4)
    teacher_detail = get_object_or_404(teacher_list, pk=1)
    context = {
        'about': about,
        'head': 'About Us',
        'title': base_view(request),
        'fun_facts': fun_facts,
        'about': about,
        'teacher_list': teacher_list,
        'teacher_detail': teacher_detail,
    }
    return render(request, 'core/about.html', context)

def contact_view(request, li):
    title = {
            'name':'Contact Us',
            'content': """Do you have other questions? Don't worry, there aren't any dumb questions. Just fill out the form below and we'll get back to you as soon as possible.
            """
        }
    context = {
        'title': title,
    }
    return render(request, 'core/'+li, context)



"""------------------------------------------------------------

                    CLASS BASED VIEWS

------------------------------------------------------------"""

class CustomList(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        m = self.object_list.get(id=1)
        context['title'] = m.header_about
        return context

class CustomDetail(DetailView):
    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['blog_reccommend'] = Blog.objects.filter(post_date__lt=date(2022,4,21))
            context['event_reccommend'] = Event.objects.filter(id__lt=4)
            context['title'] = self.object.header_about            
            context['course_reccommend'] = Course.objects.filter(Q(c_school=self.object.c_school)&~Q(id=self.object.id))
        except AttributeError:
            pass
        return context
        

