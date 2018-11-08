from django.shortcuts import redirect, render
from forms.models import Item, Form

def home_page(request):
    return render(request, 'home.html')

def view_form(request, form_id):
    form_ = Form.objects.get(id=form_id)
    return render(request, 'form.html', {'form': form_})

def new_form(request):
    form_ = Form.objects.create()
    Item.objects.create(text=request.POST['programName_text'], form=form_)
    return redirect(f'/forms/{form_.id}/')

def add_item(request, form_id):
    form_ = Form.objects.get(id=form_id)
    Item.objects.create(text=request.POST['programName_text'], form=form_)
    return redirect(f'/forms/{form_.id}/')
# Create your models here testd.