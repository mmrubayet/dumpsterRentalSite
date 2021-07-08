from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Faq
from state.models import State


class IndexView(ListView):
    model = State
    queryset = model.objects.all().order_by('name')
    template_name = 'index.html'


class HomePageView(ListView):
    model = State
    queryset = model.objects.all().order_by('name')
    template_name = 'home.html'


class StateDetailView(DetailView):
    model = State
    template_name = 'state_detail.html'
        

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
