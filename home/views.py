from django.shortcuts import render
from .forms import ContactForm

def home(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        'form' : form
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def teacher(request):
    return render(request, 'teacher.html')