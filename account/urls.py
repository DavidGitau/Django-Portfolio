from django.urls import path
from .views import login_view, create_view, logout_view, profile_view, profile_edit, EditUser

app_name = 'account'
urlpatterns = [    
    path('login/', login_view, name='login'),
    path('create-user/', create_view, name='create-user'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit/<slug:slug>/', EditUser.as_view(), name='edit')
]