import uuid
import json
from django.core import serializers
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from abet_form.abet_model_utils.abet_model_utils import abet_model_util
from abet_form.models import Application, User


def test_routing(request):
    return HttpResponse("YAY we actually work!!!")


def get_application(request, application_id):
    return HttpResponse("Looking up Application ID %s" % application_id)


def test_post(request):
    if request.method == 'POST':
        return HttpResponse("=====you_reached_a_post=====")
    return HttpResponse("=====error=====")


def get_application(request, guid):
    app = Application.objects.filter(id=guid)
    ser_obj = serializers.serialize("json", app)
    return HttpResponse(ser_obj)


def update(request, guid):
    if request.method == 'POST':
        for key, value in request.POST.items():
            print("key %s <--> value %s" % (key,value))
    return HttpResponse(guid)


@csrf_exempt
def form_submit(request):
    cur_user = User.objects.first()
    if request.method == 'POST':
        util = abet_model_util()
        if util.is_json(json_in=request.body):
            print("TIME FOR JSON")
            received_json_data = json.loads(request.body)
            print(received_json_data)
        else:
            print("TIME FOR HTML")
            for key, value in request.POST.items():
                print("key %s <--> value %s" % (key,value))
            util = abet_model_util()
            app = Application(user=cur_user)
            app.user = cur_user
            util.transform_from_post_response(request, app)
            app.save()
        all_apps = Application.objects.filter(user=cur_user)
    else:
        all_apps = Application.objects.filter(user=cur_user)
    return render(request, 'details.html', {'all_apps': all_apps})
