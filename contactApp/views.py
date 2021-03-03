from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.


def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            return redirect('/contact/?valid')
    return render(request, 'contactApp/contact.html', {'myForm': contact_form})
