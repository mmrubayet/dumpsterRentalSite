from django.views.generic import TemplateView, ListView

from .models import Faq

class IndexView(TemplateView):
    template_name = 'index.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

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
