from django.shortcuts import render
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data, e.g., send an email
            pass
    else:
        form = ContactForm()

    return render(request, 'main/index.html', {'form': form})
