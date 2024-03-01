from django.shortcuts import render,redirect
from url_shortner.models import Url
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login') 
def dashBoard(request):
    if request.user.is_authenticated:  # Check if user is authenticated
        dashboard = Url.objects.filter(user=request.user)
        context = {'dashboard': dashboard, 'user': request.user}
        return render(request, 'dashboard/dashboard.html', context)
    else:
        return redirect('login')
    
@login_required(login_url='login')    
def urlDelete(request,pk):
    urlobj = Url.objects.get(url_id=pk)
    # context = {'urlobj':urlobj}
    if request.method == 'POST':
        urlobj.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/url_del_confirmation.html')
