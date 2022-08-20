from django.shortcuts import redirect, render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from educenter.models import (
    About, 
    Blog, 
    Course
)
from .forms import (
    AboutForm, 
    BlogForm, 
    CourseForm, 
    EventForm,
    NoticeForm, 
    ResearchForm, 
    ScholarshipForm, 
    TeacherForm
)


def home(request):
    return render(request, 'educenter/be/home.html', {})


"""-------------------------------------------------------

            CLASS BASED VIEWS

-------------------------------------------------------"""

class CustomCreate(CreateView, ListView):
    # model = AboutForm
    # form_class = AboutForm
    # template_name = 'be/about.html'
    # fields = '__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plat'] = 'be'

        return context

class CustomDetail(DetailView):
    pass

