from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
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



# Decorator Class 
class Decorator(object):
    """Simple decorator class."""

    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        user = request.user
        if not user.is_staff:
            return redirect('educenter:home')
        else:
            return self.func(request, *args, **kwargs)

@Decorator
def home(request):
    # check(request)
    user = request.user
    if not user.is_staff:
        return redirect('educenter:home')
    return render(request, 'educenter/be/home.html', {'plat' : 'backend'})


"""-------------------------------------------------------

            CLASS BASED VIEWS

-------------------------------------------------------"""

class CustomCreate(CreateView, ListView):
    @method_decorator(Decorator)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plat'] = 'backend'

        return context

class CustomDetail(DetailView):
    @method_decorator(Decorator)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plat'] = 'backend'
        context['platd'] = 'backend-d'

        return context

class CustomEdit(UpdateView):
    fields = '__all__'
    template_name = 'educenter/be/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plat'] = 'backend'
        context['platd'] = 'backend-d'
        return context
