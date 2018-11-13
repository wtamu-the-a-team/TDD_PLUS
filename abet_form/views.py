from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from abet_form.models import Application


def home_page(request):
    if request.method == 'POST':
        print("Trying to do a POST")
    return render(request, 'home.html')


def get_application(request, application_id):
    return HttpResponse("Looking up Application ID %s" % application_id)


def test(request, application_id):
    # application_ = Abet_Form.objects.get(id=application_id)
    # return render(request, 'details.html', {'abet_form': application_})
    return HttpResponse("Looking up Application ID....test")
