from django.shortcuts import render
from django.core.mail import  EmailMessage
from django.conf import settings

from .forms import contactForm
# Create your views here.


def contact(request):
    title='Contact'
    form = contactForm(request.POST or None)
    context={'title':title,'form':form,}

    if form.is_valid():
        name = form.cleaned_data['name']
        comments = form.cleaned_data['comments']
        subject = 'Message from MYSITE.com'
        message = '%s %s ' %(comments, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        EmailMessage(subject, message, emailFrom, emailTo)

        title ="Thanks!"
        confirm_message="Thanks for the message.We will get back to you soon"
        context={'title':title,'confirm_message':confirm_message,}

    template = 'contact.html'
    return render(request,template,context)
