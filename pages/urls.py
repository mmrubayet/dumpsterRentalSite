from django.urls import path

from .views import (
    IndexView,
    HomePageView,
    AboutPageView,
    ServicesPageView,
    FAQPageView,
    ContactPageView,
    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('faqs/', FAQPageView.as_view(), name='faqs'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]