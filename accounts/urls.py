from django.contrib.auth.views import LoginView
from django.urls import path, include

from accounts.views import user_profile, RegisterView, SignOutView

urlpatterns = (
    path('signin/', LoginView.as_view(template_name='registration/login.html'), name='signin user', ),
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    # path('signup/', signup_user, name='signup user'),
    path('signup/', RegisterView.as_view(), name='signup user'),
    # path('signout/', signout_user, name='signout user'),
    path('signout/', SignOutView.as_view(), name='signout user'),
)

from .receivers import *
