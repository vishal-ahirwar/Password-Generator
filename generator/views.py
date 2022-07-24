from random import randint, random
from django.http import HttpResponse
from django.shortcuts import render
from random import choice,randint
# Create your views here.
def home(request):
    return render(request,"generator/index.html")

def password(request):
    length=int(request.GET.get('length'))
    
    should_include_char=bool(request.GET.get('should_include_char'))
    characters="abcdefghijklmnopqrstuvwxyz";
    n_c=[should_include_char,characters]
    password_=''
    if(should_include_char==True):

        for _ in range(length):
            c=choice(n_c)
            if(c==should_include_char):
                password_+=str(randint(0,9))
            else:
                password_+=choice(c)
    else:
        for _ in range(length):
            password_+=str(randint(0,9))

        
    return render(request,"generator/password.html",{"password":password_})

def about(request):
    return render(request,"generator/about.html")
