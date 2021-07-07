from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'

class FAQPageView(TemplateView):
    template_name = 'faqs.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'
