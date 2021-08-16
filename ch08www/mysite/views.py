from django.shortcuts import render

# Create your views here.
def index(request):
    global urpass
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid=None
    if urid is not None and urpass == '123456':
        verified = True
    else:
        verified = False
    years = range(1960, 2021)
    return render(request, 'index.html', locals())