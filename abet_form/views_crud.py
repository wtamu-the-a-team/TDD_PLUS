import uuid
import json
from email._header_value_parser import get_token

from django.core import serializers
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from abet_form.abet_model_utils.abet_model_utils import abet_model_util
from abet_form.models import Application, User
from abet_form_utils import abet_model_json_helper


def test_routing(request):
    return HttpResponse("YAY we actually work!!!")


def test_simple_url_post(request):
    if request.method == 'POST':
        return HttpResponse("=====you_reached_a_post=====")
    return HttpResponse("=====error=====")


def get_application_json(request, guid):
    app = Application.objects.filter(id=guid)
    ser_obj = serializers.serialize("json", app)
    return HttpResponse(ser_obj)


# Update Application
def update(request, guid):
    if request.method == 'POST':
        for key, value in request.POST.items():
            print("key %s <--> value %s" % (key, value))
    return HttpResponse(guid)


# Add Application
@csrf_exempt
def add_application(request, user_id):
    # print("add_application: user_id -> %s" % user_id)
    user = User.objects.get(uuid_id=user_id)
    if request.method == 'POST':
        app = Application(user=user)
        app.save()
    else:
        return HttpResponse("Sorry, we don't support application GET submissions")
    all_apps = Application.objects.filter(user=user)
    return render(request, 'details.html', {'all_apps': all_apps})


# View all Applications
@csrf_exempt
def view_user_applications(request, user_id):
    csrf_token = get_token(request)
    csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)
    # print("view_user_applications: user_id -> %s" % user_id)
    user = User.objects.get(uuid_id=user_id)
    all_apps = Application.objects.filter(user=user)
    return render(request, 'details.html', {'all_apps': all_apps})


@csrf_exempt
def form_submit(request):
    cur_user = User.objects.first()
    # print("Current User ID -> %s" % str(cur_user.uuid_id))
    if request.method == 'POST':
        util = abet_model_util()
        if util.is_json(json_in=request.body):
            print("TIME FOR JSON")
            received_json_data = json.loads(request.body)
            print(received_json_data)
        else:
            print("TIME FOR HTML")
            for key, value in request.POST.items():
                print("key %s <--> value %s" % (key, value))
            util = abet_model_util()
            app = Application(user=cur_user)
            app.user = cur_user
            util.transform_from_post_response(request, app)
            app.save()
        all_apps = Application.objects.filter(user=cur_user)
    else:
        all_apps = Application.objects.filter(user=cur_user)
    return render(request, 'details.html', {'all_apps': all_apps})


@csrf_exempt
def remove_application(request, app_id):
    app = Application.objects.filter(id=app_id).first()
    if app is None:
        return HttpResponse("Sorry, that application doesn't exist")
    else:
        app.delete()
        all_apps = Application.objects.filter(user=app.user)
        return render(request, 'details.html', {'all_apps': all_apps})


@csrf_exempt
def get_application(request, app_id):
    apps = Application.objects.filter(id=app_id)
    if apps.count() is 0:
        return HttpResponse("Sorry, Unknown Application ID")
    return render(request, 'details.html', {'all_apps': Application.objects.filter(id=app_id)})


@csrf_exempt
def update_application(request):
    if request.method == 'POST':
        print("We have a POST")
        cur_id = request.POST.getlist('id')[0]
        if cur_id is None:
            return HttpResponse("Please use a valid Application ID")
        helper = abet_model_json_helper.abet_model_json_helper()
        app = Application.objects.filter(id=cur_id).first()
        for key, value in request.POST.items():
            print("key %s <--> value %s" % (key, value))
            helper.update_model_from_json_element(app, key, value)
        print(app.job_title)
        app.save()
        return render(request, 'details.html', {'all_apps': Application.objects.filter(id=app.id)})
    else:
        return HttpResponse("Sorry, we don't support application GET updates")
