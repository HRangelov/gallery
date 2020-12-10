from django.urls import path

from common.views import LandingPageView

urlpatterns = [
    # path('', landing_page, name='index'),
    path('', LandingPageView.as_view(), name='index'),
]
