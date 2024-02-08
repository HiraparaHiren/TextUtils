from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    char_count = request.POST.get('char_count','off')
    # print(djtext)
    # print(removepunc)

    if removepunc == 'on':
        punctuation = '''!()-[]{};:'"\<>./?@#$%^&*_~'''

        analyzed = ""

        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {'purpose':'Remove Punctuation','analyzed':analyzed}

        #Analyze the text :
        # return render(request, 'analyze.html',params)
        djtext = analyzed


    if (fullcaps=='on'):
        analyzed = ""
        for char in djtext:

            analyzed = analyzed + char.upper()

        params = {'purpose':'Upper Case','analyzed':analyzed}

#         return render(request, 'analyze.html',params)
        djtext = analyzed

    if (newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose':'New Line Remove','analyzed':analyzed}

#         return render(request, 'analyze.html',params)
        djtext = analyzed
    if (extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed+char

        params = {'purpose':'Extra Space Remove','analyzed':analyzed}

#         return render(request, 'analyze.html',params)
        djtext = analyzed
    if (char_count=='on'):
        analyzed = ""
        a = []
        for index, char in enumerate(djtext):

            if (djtext[index] != " "):
                a.append(1)
        analyzed = sum(a)



        params = {'purpose':'Text','analyzed':analyzed}


#         return render(request, 'analyze.html',params)
        djtext = analyzed

    if (removepunc != 'on' and fullcaps!='on' and char_count!='on' and newlineremover!='on' and extraspaceremover!='on' ):
        return HttpResponse(djtext)

    return render(request, 'analyze.html', params)
