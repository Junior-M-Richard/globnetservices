from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 rounded', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 rounded', 'placeholder': 'Votre email'}),
            'subject': forms.TextInput(attrs={'class': 'w-full p-2 rounded', 'placeholder': 'Sujet'}),
            'message': forms.Textarea(attrs={'class': 'w-full p-2 rounded', 'placeholder': 'Votre message', 'rows': 5}),
        }
