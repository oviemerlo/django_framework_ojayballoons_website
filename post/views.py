from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.core.mail import send_mail
from django.http import HttpResponse



# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = "home.html"


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', ''),
        message = request.POST.get('message', '')

        #send email using django send mail function
        send_mail(
            'Contact Form Submission',
            'Name: {}\nEmail: {}\nPhone: {}\nMessage: {}'.format(name, email, phone, message),
            'from@ojayballoons@yahoo.com',
            ['to@ojayballoons@yahoo.com'],
            fail_silently=False,
        ) 
        return HttpResponse('Form submission successful. Thank you!') 

    return render(request, 'contact.html')



