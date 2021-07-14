from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

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


class StateListView(ListView):
    model = State
    queryset = model.objects.all().order_by('name')
    template_name = 'state_list.html'

class StateDetailView(DetailView):
    context_object_name = 'state_detail_city'
    template_name = 'state_detail.html'
    queryset = State.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StateDetailView, self).get_context_data(**kwargs)
        context['states'] = State.objects.all()
        context['cities'] = City.objects.all()
        return context

class CityDetailView(DetailView):
    model = City
    template_name = 'city_detail.html'


class SearchResultsView(ListView):
    model = City
    template_name = 'search_result.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = City.objects.filter(city_name__icontains=query)
        # object_list = City.objects.filter(
        # Q(city_name__icontains=query) | Q(state_name__icontains=query) )
        print(object_list)
        return object_list


class ServicesPageView(ListView):
    model = State
    queryset = model.objects.all().order_by('name')
    template_name = 'services.html'



class AboutPageView(TemplateView):
    template_name = 'about.html'


class FAQPageView(ListView):
    model = Faq
    template_name = 'faqs.html'


class FAQDetailView(DetailView):
    model = Faq
    template_name = 'faq_detail.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
