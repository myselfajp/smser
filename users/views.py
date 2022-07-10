from django.shortcuts import render
from django.shortcuts import redirect ,render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# Create your views here.
def http_panel_home(request):
    return render(request,'signin.html')


def http_login (request):
    if not request.user.is_authenticated:
        error=''
        if request.method == 'POST':
            number=request.POST.get('phone_number').strip()
            if len(number) == 11 and number[0:2]=="09":
                print("okyeee?")
                try:
                    user=CustomUser.objects.get(phone_number=number)
                except:
                    user=None
                if user:

                    user.code.save()
                    request.session["pk"]=user.pk
                    return redirect("verify")
                else:

                    user=CustomUser()
                    user.phone_number=request.POST.get('phone_number').strip()
                    user.username=request.POST.get('phone_number').strip()
                    user.first_name=request.POST.get('first_name').strip()
                    user.password="ABC!@#123#@!321def"
                    user.save()
                    request.session["pk"]=user.pk
                    return redirect ("verify")

            else:
                error="شماره وارد شده صحیح نیست!<br>نمونه شماره صحیح: 09121234567"

    else:
        return redirect("profile")

    return render(request,'signin.html',{"error":error})



def http_verify (request):
    pk=request.session.get("pk")
    user=CustomUser.objects.get(pk=pk)
    code=user.code
    print(code)
    error=''
    if request.method == 'POST':
        num=request.POST.get('code_num')
        if num == str(code) :
            login(request,user)
            return redirect("profile")
        else:
            error="کد وارد شده صحیح نیست دوباره امتحان کنید!"

    return render(request,'verify.html',{"error":error})
    

@login_required
def http_profile(request):
    pk=request.session.get("pk")
    user=CustomUser.objects.get(pk=pk)
    name=f"{user.first_name} عزیز سلام"

    return render(request,'profile.html',{"name":name})













    # return render(request,'signin.html')
    #         user = authenticate(request,username=user_name,password=password)
    #         if user:
    #             messages.success(request,'Login successfull .')
    #             return redirect('/')
    #         else:
    #             messages.error(request,"username or password is incorrect.")
    # else:
    #     return redirect('/')
    # return render(request, 'accounts/login.html')