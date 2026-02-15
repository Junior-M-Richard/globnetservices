from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # enregistre directement le message
            return redirect('contact-success')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'core/contact_success.html')

from django.shortcuts import render
from blog.models import BlogPost  # si tu veux afficher les derniers blogs

def home(request):
    latest_blogs = BlogPost.objects.order_by('-date_posted')[:6]  # si tu as des blogs
    return render(request, 'core/home.html', {'latest_blogs': latest_blogs})

