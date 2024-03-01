from django.shortcuts import render,redirect
import random
import string
from .models import Url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  


# Create your views here.


        
@login_required(login_url='login')     
def urlView(request):
    shorturl = None
    longurl = None 
    if request.method == 'POST':
        longurl = request.POST['link']
        print(longurl)
        alpha = string.ascii_lowercase + string.digits
        shorturl = ''
        for i in range(1,7):
           characters = random.randint(0,len(alpha)-1)           
           new_char = alpha[characters]           
           shorturl += new_char
        urlobj = Url.objects.create(url=longurl, short_url=shorturl, user=request.user) 
        shorturl = "http://127.0.0.1:8000/" + shorturl
        print(shorturl)
            
    return render(request, 'url_shortner/url.html',context={"shorturl":shorturl,"longurl":longurl})

@login_required(login_url='login') 
def redirecturl(request, shorturl):
    # print(shorturl)
    try:
        obj = Url.objects.get(short_url=shorturl)
    except Url.DoesNotExist:
        obj = None    
    
    if obj is not None:
        # print('object found')
        # print(obj.url)
        return redirect(obj.url)

    else:
        return HttpResponse("check your url")
       

    
