from django.urls import path, include
from .forms import (
    AboutForm,
    BlogForm,
    CourseForm,
    EventForm,
    FunFactForm,
    InterestForm,
    NoticeForm,
    RequirementForm,
    ResearchForm,
    ScholarshipForm,
    SchoolForm,
    TeacherForm
)

from educenter.models import (
    About,
    Blog,
    Course,
    Event,
    FunFact,
    Interest,
    Notice,
    Requirement,
    Research,
    Scholarship,
    School,
    Teacher
)

from .views import (
    home,
    CustomCreate,
    CustomDetail,
    # about, 
    # blog, 
    # course, 
    # event,
    # notice, 
    # research, 
    # scholarship, 
    # teacher,
)

li0 = [
    'about',
    'blog',
    'course',
    'event',
    'funfact',
    'interest',
    'notice',
    'requirement',
    'research',
    'scholarship',
    'school',
    'teacher'
]


li1 = [
    About,
    Blog,
    Course,
    Event,
    FunFact,
    Interest,
    Notice,
    Requirement,
    Research,
    Scholarship,
    School,
    Teacher
]

li2 = [
    AboutForm,
    BlogForm,
    CourseForm,
    EventForm,
    FunFactForm,
    InterestForm,
    NoticeForm,
    RequirementForm,
    ResearchForm,
    ScholarshipForm,
    SchoolForm,
    TeacherForm
]

length1 = [0, 1, 2, 3, 6, 8, 9, 11]
length2 = [4, 5, 7, 10]

app_name = 'backend'


urlpatterns = [
    path('', home, name='home'),
    path('account/', include('account.urls', namespace='b-account')),
]

for l in length1:
    urlpatterns.append(
        path(
                f"{li0[l]}/",
                CustomCreate.as_view(
                    model = li1[l],
                    form_class = li2[l],
                    template_name = f"educenter/core/{li0[l]}.html", 
                    success_url = f"#",
                ),
                name = f"{li0[l]}"
            )
    ),
    urlpatterns.append(
        path(
                f"{li0[l]}/<int:pk>/",
                CustomDetail.as_view(
                    model = li1[l],
                    template_name = f"educenter/core/{li0[l]}-single.html", 
                ),
                name = f"{li0[l]}-single"
            )
    )

for l in length2:
    urlpatterns.append(
        path(
                f"{li0[l]}/",
                CustomCreate.as_view(
                    model = li1[l],
                    form_class = li2[l],
                    template_name = "educenter/be/list.html", 
                    success_url = f"#",
                ),
                name = f"{li0[l]}"
            )
    ),
    urlpatterns.append(
        path(
                f"{li0[l]}/<int:pk>/",
                CustomDetail.as_view(
                    model = li1[l],
                    template_name = f"educenter/be/detail.html", 
                ),
                name = f"{li0[l]}-single"
            )
    )