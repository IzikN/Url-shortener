
from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLForm
from .models import URL

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            return render(request, 'success.html', {'short_url': url.short_url})
    else:
        form = URLForm()
    return render(request, 'home.html', {'form': form})

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)
