from django.http import HttpResponse
from django.shortcuts import render
import operator

"""def home(request):
    return HttpResponse("Hello")"""

def home(request):
    return render(request, "home.html")

def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()

    wordcount = {}
    for word in wordlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    sorted_words = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {"fulltext":fulltext, "count": len(wordlist), "wordcount":sorted_words})

