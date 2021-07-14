from django.urls import path

from .views import (
    IndexView,
    HomePageView,
    AboutPageView,
    ServicesPageView,
    FAQPageView,
    ContactPageView,

    FAQDetailView,
    StateListView,
    StateDetailView,
    CityDetailView,
    SearchResultsView,
    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('faqs/', FAQPageView.as_view(), name='faqs'),
    path('faqs/<int:pk>/', FAQDetailView.as_view(), name='faq_detail'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('service_area/', StateListView.as_view(), name='state_list'),
    path('<slug:slug>', StateDetailView.as_view(), name='state_detail'),
    path('city/<slug:slug>', CityDetailView.as_view(), name='city_detail'),

    path('search/', SearchResultsView.as_view(), name='search_result'),

]
