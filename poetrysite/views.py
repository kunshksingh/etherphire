from django.shortcuts import render
from django.http import HttpResponse
from .models import *
#from organizeData import addSpace

def mainPage(request):
    return render(request, 'mainPage.html')

def poetry(request):
    return render(request, 'poetry.html')

def allPoetry(request, scrapped):
    items = Poems.objects.all()
    
    poemNames = []
    poemTexts = []
    tags = []
    

    counter = 0
    
    if (scrapped):
        for poem in reversed(items):
            if (poem.scrap == "FALSE" or poem.scrap is None):
                continue

            poemNames.append(poem.poem_name)
            poemTexts.append(poem.poem)
            tags_list = poem.tags.split(',')
            tags.append(tags_list)
    else:
        for poem in reversed(items):
            if (poem.scrap == "TRUE"):
                continue
            poemNames.append(poem.poem_name)
            poemTexts.append(poem.poem)
            tags_list = poem.tags.split(',')
            tags.append(tags_list)

    return render(request, 'allPoetry.html', {'poemNames':poemNames,'poemTexts':poemTexts,'tags':tags})

def preface(request):
    return render(request, 'preface.html')

def blog(request):
    return render(request, 'blog.html')
def automation(request):
    return render(request, 'automaticPoet.html')
def poem(request, poemname):
    if (poemname == "scrapped"):
        return allPoetry(request, True)
    if (poemname == "main"):
        return allPoetry(request, False)
    items = Poems.objects.all()
    for object in items:
        if object.poem_name.strip() == poemname.strip():
            #object.poem = addSpace(object.poem)

            return render(request, 'poem.html', {
'poemName': object.poem_name,'poemText': object.poem, 'tags':object.tags
    })
    return render(request, 'nonePage.html')



