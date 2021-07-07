from django.urls import path

from .views import (
    IndexView,
    HomePageView,
    AboutPageView,
    ServicesPageView,
    FAQPageView,
    ContactPageView,

    StateDetailView,
    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicesPageView, name='services'),
    path('faqs/', FAQPageView.as_view(), name='faqs'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('<slug:slug>', StateDetailView.as_view(), name='state_detail'),

]
