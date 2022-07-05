from django.shortcuts import render

# Create your views here.
def http_panel_home(request):
    
    return render(request,'signin.html')
