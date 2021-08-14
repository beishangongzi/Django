from django.shortcuts import render
from datetime import datetime

# Create your views here.
def engtv(request, tvno='0'):
    tv_list = [{'name': "SkyNews", 'tvcode': 'y60wDzZt8yg'}]
    now = datetime.now()
    tv = tv_list[int(tvno)]
    hour = now.timetuple().tm_hour
    return render(request, "engtv.html", locals())

