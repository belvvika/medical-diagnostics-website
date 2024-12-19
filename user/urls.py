from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.apps import UserConfig
from user.views import UserCreateView, email_verification, ProfileView, UserModeratorView, UserListView

app_name = UserConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('', UserListView.as_view(), name='user_list'),
    path('update/<int:pk>/', UserModeratorView.as_view(template_name='user/user_update.html'), name='user_update'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
