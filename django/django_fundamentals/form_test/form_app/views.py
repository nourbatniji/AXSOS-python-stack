from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_user(request):
    print(request.POST)
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    print(request.POST)
    context = {
        'name' : name_from_form,
        'email' : email_from_form
    }
    return redirect('/success')


def success(request):
    return render(request, 'show.html')
