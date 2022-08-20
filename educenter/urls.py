from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .models import (
    Blog,
    Course,
    Event,
    Notice,
    Research,
    Scholarship,
    Teacher
)
from .views import (
    about_view, 
    # blog_view, 
    # teacher_view, 
    contact_view,
    # course_view, 
    home_view, 
    # notice_view, 
    # event_view, 
    # research_view, 
    # scholarship_view,
    CustomList,
    CustomDetail
)

app_name = "user"
# from .views import home_view

li1 = [
    Blog,
    Course,
    Event,
    Notice,
    Research,
    Scholarship,
    Teacher,
]

li2 = [
    'blog',
    'course',
    'event',
    'notice',
    'research',
    'scholarship',
    'teacher',
]

length = [0, 1, 2, 3, 4, 5, 6]
length1 = [0, 1, 2, 3, 6]

urlpatterns = [
        path('', home_view, name='home'),
        path('about/', about_view, name='about'),
        path('account/', include('account.urls', namespace='u-account')),
        path('be/', include('eduback.urls')),
        path('contact/account/', include('account.urls', namespace='ac-account')),
        path('about/account/', include('account.urls', namespace='ab-account')),
        path('contact/', contact_view, {'li':'contact.html'}, name='contact' ),

        # path('blog-single/<int:pk>', blog_view, {'li':'blog-single.html'}, name='blog-single' ),
        # path('blog/', blog_view, {'li':'blog.html'}, name='blog' ),
        
        # path('teacher-single/<int:pk>', teacher_view, {'li':'teacher-single.html'}, name='teacher-single' ),
        # path('teacher/', teacher_view, {'li':'teacher.html'}, name='teacher' ),
        
        # path('notice-single/', notice_view, {'li':'notice-single.html'}, name='notice-single' ),
        # path('notice/', notice_view, {'li':'notice.html'}, name='notice' ),
        
        # path('course-single/<int:pk>', course_view, {'li':'course-single.html'}, name='course-single' ),
        # path('courses/', course_view, {'li':'courses.html'}, name='courses' ),
        
        # path('event-single/<int:pk>', event_view, {'li':'event-single.html'}, name='event-single' ),
        # path('events/', event_view, {'li':'events.html'}, name='events' ),

        # path('research/', research_view, {'li':'research.html'}, name='research' ),
        # path('scholarship/', scholarship_view, {'li':'scholarship.html'}, name='scholarship' ),

        # path(
        #     'teacher/', 
        #     CustomList.as_view(
        #         model = Teacher,
        #         template_name = 'core/teacher.html'
        #     ), 
        #     name = 'teacher'
        # ),
        # path(
        #     'teacher-single/<int:pk>',
        #     CustomDetail.as_view(
        #         model = Teacher,
        #         template_name = 'core/teacher-single.html'
        #     ),
        #     name = 'teacher-single'
        # ),
    ]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

for i in length :
    urlpatterns.append(
        path(
            li2[i]+'/', 
            CustomList.as_view(
                model = li1[i],
                template_name = 'core/'+li2[i]+'.html'
            ), 
            name = li2[i]
        )      
    )

for n in length1:
    urlpatterns.append(
        path(
            li2[n]+'-single/<int:pk>',
            CustomDetail.as_view(
                model = li1[n],
                template_name = 'core/'+li2[n]+'-single.html'
            ),
            name = li2[n]+'-single'
        )
    )