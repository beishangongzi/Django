from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.


def index(request):
    posts = Post.objects.filter(enabled=True).order_by("-pubDate")[:30]
    # posts = Post.objects.filter(enabled=True)
    moods = Mood.objects.all()
    try:
        userId = request.GET["userId"]
        userPass = request.GET["userPass"] if request.GET["userPass"] != "" else 123
        userPost = request.GET["userPost"]
        userMood = request.GET["mood"]
        mood = Mood.objects.get(status=userMood)
        post = Post.objects.create(mood=mood, nickName=userId, delPass=userPass, message=userPost)
        post.save()
        return redirect("mysite:view-index")
    except:
        message = 'Every blank should be not null.'
    return render(request, 'index.html', {"posts": posts, "message": message, "moods": moods})


