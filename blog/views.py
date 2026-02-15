from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # <-- Sauvegarde le message en base !
            return redirect('home')  # ou afficher un message de succès
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
