from django.shortcuts import redirect, render

def home_page(request):
    if request.method == 'POST':
        print("Trying to do a POST")
    return render(request, 'home.html')
