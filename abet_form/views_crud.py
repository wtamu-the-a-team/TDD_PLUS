import uuid
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
    #     application_ = Abet_Form.objects.create()
    #     programNameInput_ = "TESTER Program"
        ## request.POST is not pulling the data.  It crashes when the line below is uncommented.
        #Application.objects.create(program_name=request.POST['input_9'], abet_form=application_) 
        # Application.objects.create(program_name=programNameInput_, abet_form=application_)
        # return redirect(f'/abet_form/{application_.id}/')
        #return HttpResponse(f'=====you_reached_a_post with Application ID# {application_.id}+{programNameInput_}====')

    return HttpResponse("=====error=====")


@csrf_exempt
def details(request):
    if request.method == 'POST':
        print ("Pass")
        user = User()
        user.save()
        cur_user = User.objects.first()
        util = abet_model_util()
        app = Application(user=cur_user)
        app.user = cur_user
        util.transform_from_post_response(request, app)
        app.save()
        app.save()
        all_apps = Application.objects.filter(user=cur_user)
        print(all_apps.count())
        for i in all_apps:
            print(i.id)

    return render(request, 'details.html',{'all_apps':all_apps})
