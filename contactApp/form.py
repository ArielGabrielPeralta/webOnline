from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Your name", required=True, max_length=100)
    email = forms.CharField(label="Email", required=True,
                            widget=forms.EmailInput(attrs={'type': 'email'}))
    content = forms.CharField(label="Content", widget=forms.Textarea)
