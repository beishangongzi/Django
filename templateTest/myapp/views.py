from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request, tvno=0):
    now = datetime.now()
    tv_list = [{'name': 'taylor', 'tvcode': 'BtFSokmpcV4'},
            ]
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())
