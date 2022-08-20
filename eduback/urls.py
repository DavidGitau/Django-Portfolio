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


# li3 = [
#     'be/about.html',
#     'be/blog.html',
#     'be/course.html',
#     'be/event.html',
#     'be/funfact.html',
#     'be/interest.html',
#     'be/notice.html',
#     'be/requirement.html',
#     'be/research.html',
#     'be/scholarship.html',
#     'be/school.html',
#     'be/teacher.html'
# ]

length = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

app_name = 'backend'


urlpatterns = [
    path('', home, name='home'),
    path('account/', include('account.urls', namespace='b-account'))
    # path('about/', about, name='about'),
    # path(
    #     'about/',
    #     CustomCreate.as_view(
    #         model = li1[0],
    #         form_class = li2[0],
    #         template_name = li3[0]
    #     ),
    #     name = 'about'
    # ),

    # path('blog', blog, name='blog'),
    # # path(

    # # ),

    # path('course/', course, name='course'),
    # path('event/', event, name='event'),
    # path('notice/', notice, name='notice'),
    # path('research/',research , name='research'),
    # path('scholarship/', scholarship, name='scholarship'),
    # path('teacher/', teacher, name='teacher'),
]

for l in length:
    urlpatterns.append(
        path(
                f"{li0[l]}/",
                CustomCreate.as_view(
                    model = li1[l],
                    form_class = li2[l],
                    template_name = f"core/{li0[l]}.html", 
                    success_url = f"#",
                ),
                name = f"{li0[l]}"
            )
    ),
    urlpatterns.append(
        path(
                f"{li0[l]}/<int:id>/",
                CustomDetail.as_view(
                    model = li1[l],
                    template_name = f"core/{li0[l]}-single.html", 
                ),
                name = f"{li0[l]}"
            )
    )

