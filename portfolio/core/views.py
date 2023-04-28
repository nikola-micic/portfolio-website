from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from core.models import Project
from django.core.mail import send_mail, BadHeaderError
from core.forms import ContactForm
from mimetypes import *
from wsgiref.util import FileWrapper
import os
# Create your views here.

def index(request):
    return render(request, 'index.html')

def projects(request):
    context = {}
    projects = Project.objects.all()
    context['projects'] = projects
    return render(request, 'projects.html', context=context)

def detail(request, id):
    context={}
    projects = Project.objects.all()
    for project in projects:
        if project.id == id:
            context["project"] = project
    return render(request, 'detail.html', context=context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Message"
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email_address"],
                "phone": str(form.cleaned_data["phone_number"]),
                "country": form.cleaned_data["country"],
                "title": form.cleaned_data["title"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, form.cleaned_data["email_address"], ["djangobre7@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect ("success")
        return render(request, 'contact.html', {'form': form})
    
    context = {}
    form = ContactForm()
    context['form'] = form
    return render(request, 'contact.html', context=context)

def success(request):
    return render(request, 'success.html')

def download_cv(request):
    mt_instance = MimeTypes()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = "NikolaCV.pdf"
    filepath = base_dir + "/files/" + filename
    cv = filepath
    filename = os.path.basename(filepath)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(cv, 'rb'), chunk_size), content_type=mt_instance.guess_type(cv)[0])
    response['Content-Length'] = os.path.getsize(cv)
    response['Content-Disposition'] = "Attachment;filename=%s" % filename
    return response



