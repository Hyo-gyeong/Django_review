from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    word = text.split()
    wordDict = {}

    for w in word:
        if w in wordDict:
            wordDict[w] += 1
        else:
            wordDict[w] = 1
            
    return render(request, 'result.html', {'full':text, 'wordcount':len(word), 'dictionary':wordDict.items()})