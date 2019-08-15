from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
def homepage(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")

def count(request):
    fulltext = request.GET["fulltext"]
    word_count = len(fulltext.split())
    word_dic = Counter(fulltext.split())

    return render(request,"count.html",{"fulltext":fulltext,"count":word_count,"word_dic":word_dic.items()})
