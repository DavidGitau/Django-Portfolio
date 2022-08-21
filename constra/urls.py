from django.urls import path, include 
from .views import (
    home_view,
    about_view,
    comment_view,
    contact_view,
    faq_view,
    login_view,
    logout_view,
    news_detail,
    reg_view,
    typography_view,
    view_404,
    CustomDetail,
    CustomList,
)
from .models import (
    News,
    Pricing,
    Project,
    Service,
    Team,
    Testimonial,
)

app_name = 'constra'

urlpatterns = [
    path('', home_view, name='home'),
    path('404/', view_404, name='404'),
    path('about/', about_view, name='about'),
    path('comment/', comment_view, name='comment'),
    path('contact/', contact_view, name='contact'),
    path('faq/', faq_view, name='faq'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('news/<int:id>/', news_detail, name='news-detail'),
    path('reg/', reg_view, name='reg'),
    path('typography/', typography_view, name='typography'),

    # News urls
    path(
        'news-right/', 
        CustomList.as_view(
            model = News,
            template_name = 'constra/news/news-right.html'
        ), 
        name='news-right'
        ),
    path(
        'news-left/', 
        CustomList.as_view(
            model = News,
            template_name = 'constra/news/news-left.html'
        ), 
        name='news-left'
        ),
    # path(
    #     'news/<int:pk>/', 
    #     CustomDetail.as_view(
    #         model = News,
    #         template_name = 'constra/news/detail.html'
    #     ), 
    #     name='news-detail'
    #     ),

    # Pricing url
    path(
        'pricing/', 
        CustomList.as_view(
            model = Pricing,
            template_name = 'constra/other/pricing.html'
        ), 
        name='pricing'
        ),
    
    # Project urls
    path(
        'projects/', 
        CustomList.as_view(
            model = Project,
            template_name = 'constra/project/project.html'
        ), 
        name='project'
        ),
    path(
        'project/<int:pk>/', 
        CustomDetail.as_view(
            model = Project,
            template_name = 'constra/project/detail.html'
        ), 
        name='project-detail'
        ),

    # Service urls
    path(
        'service/', 
        CustomList.as_view(
            model = Service,
            template_name = 'constra/service/service.html'
        ), 
        name='service'
        ),
    path(
        'service/<int:pk>/', 
        CustomDetail.as_view(
            model = Service,
            template_name = 'constra/service/detail.html'
        ), 
        name='service-detail'
        ),

    # Team url
    path(
        'team/', 
        CustomList.as_view(
            model = Team,
            template_name = 'constra/team/team.html'
        ), 
        name='team'
        ),

    # testimonial url
    path(
        'testimonial/', 
        CustomList.as_view(
            model = Testimonial,
            template_name = 'constra/other/testimonial.html'
        ), 
        name='testimonial'
        ),
]