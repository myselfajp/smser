from django.shortcuts import render
from django.shortcuts import redirect ,render
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .defs import code_sender
from .models import CustomUser

# Create your views here.

def http_login (request):
    if not request.user.is_authenticated:
        error=''
        if request.method == 'POST':
            number=request.POST.get('phone_number').strip()
            if len(number) == 11 and number[0:2]=="09":
                try:
                    user=CustomUser.objects.get(phone_number=number)
                except:
                    user=None
                if user:

                    user.code.save()
                    request.session["pk"]=user.pk
                    code_sender(number,user.code)
                    return redirect("verify")
                else:

                    user=CustomUser()
                    user.phone_number=number
                    user.username=number
                    user.first_name=request.POST.get('first_name').strip()
                    user.password="ABC!@#123#@!321def"
                    user.save()
                    request.session["pk"]=user.pk
                    code_sender(number,user.code)
                    return redirect ("verify")

            else:
                error="شماره وارد شده صحیح نیست!<br>نمونه شماره صحیح: 09121234567"

    else:
        return redirect("profile")

    return render(request,'signin.html',{"error":error})

def http_verify (request):
    if not request.user.is_authenticated:
        pk=request.session.get("pk")
        if pk:
            user=CustomUser.objects.get(pk=pk)
            code=user.code
        else:
            return redirect('/')
        print(code)
        error=''
        if request.method == 'POST':
            num=request.POST.get('code_num')
            if num == str(code) :
                login(request,user)
                return redirect("profile")
            else:
                error="کد وارد شده صحیح نیست دوباره امتحان کنید!"
    else:
        return redirect("profile")
    return render(request,'verify.html',{"error":error})
    
@login_required
def http_profile(request):
    pk=request.session.get("pk")
    user=CustomUser.objects.get(pk=pk)
    name=user.first_name
    charge=user.charge
    if name:
        name=f"{name} عزیز سلام"
    else:
        name="دوست عزیز سلام"
    return render(request,'profile.html',{"name":name,"charge":charge})

@login_required
def http_logout(request):
    logout(request)
    return redirect('/')
     
@login_required
def http_buy(request):
    return render(request,'buy.html')

@login_required
def http_payment(request):
    pk=request.session.get("pk")
    user=CustomUser.objects.get(pk=pk)
    user.charge=user.charge+30
    user.save()
    name=user.first_name
    charge=user.charge
    if name:
        name=f"{name} عزیز سلام"
    else:
        name="دوست عزیز سلام"
    return render(request,'profile.html',{"name":name,"charge":charge})
