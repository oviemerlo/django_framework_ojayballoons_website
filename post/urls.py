from django.urls import path
from .views import contact

from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('contact/', contact, name='contact'),
]
