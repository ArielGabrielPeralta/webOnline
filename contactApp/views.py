from django.shortcuts import render, redirect
from .form import ContactForm
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            email = EmailMessage("Message from Django App",
                                 "The user {} with the mail {} write the message:\n\n{}".format(
                                     name, email, content),
                                 "", ["agperalta80@gmail.com"], reply_to=[email])
            try:
                email.send()
                return redirect('/contact/?valid')
            except:
                return redirect('/contact/?invalid')

    return render(request, 'contactApp/contact.html', {'myForm': contact_form})
