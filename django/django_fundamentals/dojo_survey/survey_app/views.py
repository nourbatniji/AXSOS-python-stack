from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")


def create_dojo(request):
    print(request.POST)
    username = request.POST['username']
    userlocation = request.POST['userlocation']
    favlanguage = request.POST['favlanguage']
    usercomments = request.POST['usercomment']
    usergender = request.POST.get('gender')
    privacy = request.POST.get('privacy')

    context = {
        'username' : username,
        'userlocation' : userlocation,
        'favlanguage' : favlanguage,
        'usercomments' : usercomments,
        'usergender' : usergender,
        'privacyagreement' : privacy
    }

    return render(request, 'show.html', context)