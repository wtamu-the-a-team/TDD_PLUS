from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse


def test_routing(request):
    return HttpResponse("YAY we actually work!!!")


def get_application(request, application_id):
    return HttpResponse("Looking up Application ID %s" % application_id)


def test_post(request):
    if request.method == 'POST':
        return HttpResponse("=====you_reached_a_post=====")
    return HttpResponse("=====error=====")
