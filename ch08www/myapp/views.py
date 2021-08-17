from django.shortcuts import render
from django.http import HttpResponse
from myapp import models
from django.template.loader import get_template

# Create your views here.
def index(request):
    template = get_template('index.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass= request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = 'every blank is not null'
    if user_id is not None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickName=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message='save success. please remember your password'

    return render(request, 'index.html', locals())