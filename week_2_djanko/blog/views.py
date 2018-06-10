# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint
from .models import Article
# Create your views here.

def index(request):
    # rannum = randint(1, 10)
    # return HttpResponse("Hello, world. {}".format(rannum))
    # name = "namja"
    article_list = Article.objects.all() #article.objects에 있는 모든 오브젝트를 불러와라
#    Article.objects.create(
#        title = "hello",
#        contents = "this is test",
#        view_count = 0
#    )

    ctx = { #dictionary
        "article_list" : article_list
    }
    return render(request, "index.html", ctx) # view.py라는 기능이 없다면 각 페이지에 대한 템플릿을 각각 만들어야 한다.
