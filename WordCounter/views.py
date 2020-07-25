from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.POST['txtAreaWords']

    wordlist = fulltext.split()

    wordDictonary = {}

    for word in wordlist:
        if word in wordDictonary:
            wordDictonary[word] += 1
        else:
            wordDictonary[word] = 1

    sortedWordes = sorted(wordDictonary.items(), key=operator.itemgetter(1), reverse=True)

    context = {'fulltext':fulltext, 'sortedWordes':sortedWordes}
    return render(request, 'count.html', context)