from django import forms


class contactForm(forms.Form):
    name=forms.CharField(required=False,help_text='100 characters max',max_length=100)
    email=forms.EmailField(required=True)
    comments=forms.CharField(required=True,widget=forms.Textarea)
