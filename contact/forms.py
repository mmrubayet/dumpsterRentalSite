from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contactus', 'placeholder':'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'contactus', 'placeholder':'Email'}),
            'phone': forms.TextInput(attrs={'class': 'contactus', 'placeholder':'Phone Number'}),
            'location': forms.TextInput(attrs={'class': 'contactus', 'placeholder':'Desired Service Area'}),
            'message': forms.Textarea(attrs={'class': 'contactus', 'placeholder':'Message'}),
        }
