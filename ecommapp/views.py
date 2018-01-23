from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    context = {} #locals()
    template = 'home.html'
    return render(request,template,context)
def about(request):
    context = {}
    template='about.html'
    return render(request,template,context)
@login_required
def userProfile(request):
    user = request.user
    context = {'user':user}
    template='profile.html'
    return render(request,template,context)

@login_required
def checkout(request):
    context = {}
    template='checkout.html'
    return render(request,template,context)

def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None


    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from Ecomm.com'
        message = '%s %s'%(comment,name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailFrom,emailTo,fail_silently= False)
        print subject,message,emailFrom,emailTo



        title = "THANKS!!"
        confirm_message = "%s %s Thanks for the message!we will get right you back!!!" % ( emailFrom, emailTo)
        form = None

    context = {'title':title,'form':form,'confirm_message':confirm_message,}

    template='contact.html'
    return  render(request,template,context)
