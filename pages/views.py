from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Faq, State

class HomeStatesView(ListView):
    model = State
    template_name = 'home.html'
    context_object_name = 'all_states_list'


class IndexView(TemplateView):
    template_name = 'index.html'

def HomePageView(request):
    # template_name = 'home.html'
    qs = State.objects.all()
    context = {'all_states_list': qs}
    return render(request, 'home.html', context)


class AboutPageView(TemplateView):
    template_name = 'about.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'

class FAQPageView(ListView):
    model = Faq
    template_name = 'faqs.html'
    context_object_name = 'all_faqs_list'

class ContactPageView(TemplateView):
    template_name = 'contact.html'
