from django.shortcuts import render
from django.http import HttpResponse

from .models import News

# Create your views here.

def index(request):
    news = News.objects.all()
    res = '<h1>List of news</h1>'
    for item in news:
        res += f'''
        <div>
            <p>{item.title}</p>\n
            <p>{item.content}</p>\n
        <div>
        <hr>
        '''
    return HttpResponse(res)

def test(request):
    return HttpResponse('<h1>Test</h1>')