from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Faq
from state.models import State, City


class IndexView(ListView):
    model = State
    queryset = model.objects.all().order_by('name')
    template_name = 'index.html'


class HomePageView(ListView):
    model = State
    queryset = model.objects.all().order_by('name')
    template_name = 'home.html'


# class StateDetailView(DetailView):
#     model = State
#     template_name = 'state_detail.html'

class StateDetailView(DetailView):
    context_object_name = 'state_detail_city'
    template_name = 'state_detail.html'
    queryset = State.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StateDetailView, self).get_context_data(**kwargs)
        context['states'] = State.objects.all()
        context['cities'] = City.objects.all()
        # print(City.objects.all())
        # print([city.city_name for city in context['cities']])
        # print(context['object'])
        return context

class CityDetailView(DetailView):
    model = City
    template_name = 'city_detail.html'


class ServicesPageView(ListView):
    model = State
    queryset = model.objects.all().order_by('name')
    template_name = 'services.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class FAQPageView(ListView):
    model = Faq
    template_name = 'faqs.html'
    context_object_name = 'all_faqs_list'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
