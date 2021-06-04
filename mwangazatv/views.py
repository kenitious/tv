from django.shortcuts import render, redirect
from news.forms import ContactForm
from news.models import dailyhighlights, trendingnews
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views import generic


def index(request):
    highlights = dailyhighlights.objects.all()
    tnews = trendingnews.objects.all()

    # images = dailyhighlights.objects.all()

    return render(request, 'index.html', {'tnews': tnews, 'highlights': highlights})


def faqs(request):
    return render(request, 'faqs.html', {})


def sports(request):
    highlights = dailyhighlights.objects.all()

    # images = dailyhighlights.objects.all()

    return render(request, 'sports.html', {'highlights': highlights})


class post_detail(generic.DetailView):
    model = dailyhighlights
    model = trendingnews
    template_name = 'post_detail.html'



def contact(request):
    global subject
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
        body = {
            'names': form.cleaned_data['names'],
            'subject': form.cleaned_data['subject'],
            'email': form.cleaned_data['email'],
            # 'phone': form.cleaned_data['phone'],
            'message': form.cleaned_data['message'],
        }
        message = "\n".join(body.values())

        try:
            send_mail(subject, message, 'email', ['kenitiouswambuah@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect("index.html")
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def programs(request):
    return render(request, 'programs.html', {})
