from django.shortcuts import render, redirect

def index(request):
    if 'key_name' in request.session:
        request.session['key_name'] += 1 

    else:
        request.session['key_name'] = 1  

    context = {
        'numberVisits' :request.session['key_name'],

    }
    return render(request, 'index.html', context)

def destroy_session(request):
    del request.session['key_name']
    print('key cleared successfully')
    return redirect('/')

def incrementBy2(request):
    request.session["key_name"] += 2
    print("incremented successfully")
    context = {
        '2counter' : request.session["key_name"]
    }
    return render(request, 'counterBy2.html', context)

