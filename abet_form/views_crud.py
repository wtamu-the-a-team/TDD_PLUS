from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from abet_form.abet_model_utils.abet_model_utils import abet_model_util
from abet_form.models import Application

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
        util = abet_model_util()
        app = Application()
        util.transform_from_post_response(request, app)
        app.save()
        saved_items = Application.objects.all()
        print("=====Current Object Count -> %s=====" % saved_items.count())
    return render(request, 'details.html')
