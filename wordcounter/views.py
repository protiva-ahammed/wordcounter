
from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,"home.html")

def count(request):
    fulltext= request.GET["fulltext"]
    print(fulltext)
    wordlist=fulltext.split()
    worddictonary={}
    for word in wordlist:
        if word in worddictonary:
            #increase
            worddictonary[word] +=1
        else:
            #add to the dictonary
            worddictonary[word]=1
    sortedword=sorted(worddictonary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,"count.html",{'fulltext':fulltext,'count':len(wordlist),'worddictonary':sortedword})
