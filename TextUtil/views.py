from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    djtext = request.POST.get('text','default')
    punc = request.POST.get('removepunc','off')
    lineremover = request.POST.get('newlineremover','off')
    upper = request.POST.get('uppercase','off')
    spaceremover = request.POST.get('extraspaceremover','off')

    if punc=='on':     # Remove Punctuation
        punctuation='''!@#$%^&*()_-=+/*-[]{}":';><,.?/\|.'''
        anlyz=""
        for ch in djtext:
            if ch not in punctuation:
                anlyz=anlyz+ch
            
        data ={
            'purpose':'Remove Punctiation',
            'analyze':anlyz
        }
        return render(request,'analyze.html',data)
    
    elif lineremover=='on':     # New line remover
        anlyz=""
        for ch in djtext:
            if ch != '\n' and ch !='\r':
                anlyz=anlyz+ch
            
        data ={
            'purpose':'NewLineRemover',
            'analyze':anlyz
        }
        return render(request,'analyze.html',data)
    
    elif upper=='on':     # uppercase
        anlyz=""
        for ch in djtext:
                anlyz=anlyz+ch.upper()
            
        data ={
            'purpose':'UpperCase',
            'analyze':anlyz
        }
        return render(request,'analyze.html',data)
    
    elif spaceremover=='on':     # Extra space remover
        anlyz=""
        for index,ch in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                anlyz=anlyz+ch

        data ={
            'purpose':'ExtraSpaceRemove',
            'analyze':anlyz
        }
        return render(request,'analyze.html',data)
    
    
    else:
        return HttpResponse('ERROR: !!!_Select Check Box_!!!')
        
def about(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contact.html")
    