from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']  # plus de 'subject'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-3 rounded-md bg-gray-800 text-white', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-3 rounded-md bg-gray-800 text-white', 'placeholder': 'Votre email'}),
            'message': forms.Textarea(attrs={'class': 'w-full p-3 rounded-md bg-gray-800 text-white', 'placeholder': 'Votre message', 'rows': 5}),
        }
