from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    template="home.html"
    return render(request,template,context)

def about(request):
    context={}
    template="about.html"
    return render(request,template,context)

def view_details_ban(request):
    context={}
    template="ibps.html"
    return render(request,template,context)

def aipmt(request):
    context={}
    template="aipmt.html"
    return render(request,template,context)

def ics(request):
    context={}
    template="ics.html"
    return render(request,template,context)

def banking(request):
    context={}
    template="banking.html"
    return render(request,template,context)

def current_affair(request):
    context={}
    template="current_affair.html"
    return render(request,template,context)

def motivation(request):
    context={}
    template="motivation.html"
    return render(request,template,context)


def gk2017(request):
    context={}
    template="gk2017.html"
    return render(request,template,context)

def gk2016(request):
    context={}
    template="gk2016.html"
    return render(request,template,context)

def gk2015(request):
    context={}
    template="gk2015.html"
    return render(request,template,context)


def payment(request):
    context={}
    template="payment.html"
    return render(request,template,context)



def choice_of_course(request):
    context={}
    template="choice_of_course.html"
    return render(request,template,context)
















