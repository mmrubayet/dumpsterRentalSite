from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Faq, State


class IndexView(TemplateView):
    template_name = 'index.html'

def HomePageView(request):
    # template_name = 'home.html'
    qs = State.objects.all().values_list('name', named=True).order_by('name')
    context = {'all_states_list': qs}
    return render(request, 'home.html', context)


def ServicesPageView(request):
    # template_name = 'services.html'
    state_art = State.objects.all().values_list('name', 'article', named=True).order_by('name')
    context = {'state_articles': state_art}
    return render(request, 'services.html', context)


class AboutPageView(TemplateView):
    template_name = 'about.html'


class FAQPageView(ListView):
    model = Faq
    template_name = 'faqs.html'
    context_object_name = 'all_faqs_list'

class ContactPageView(TemplateView):
    template_name = 'contact.html'
