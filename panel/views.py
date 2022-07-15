from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from users.models import CustomUser
from .defs import energy_sender,need_charge
from django.db.models import F

# Create your views here.
@login_required
def send_sms(request):
    admin=request.user.phone_number
    if admin in ["09057392369","09195035763"]:

        actives=CustomUser.objects.filter(charge__gte=1)
        numbers=list(map(lambda x:x.phone_number,actives)) #get list of all actives members

        need_charges=CustomUser.objects.filter(charge__lte=1)
        need_charge_numbers=list(map(lambda x:x.phone_number,need_charges))

        messege=f"پیام شما برای {len(actives)} نفر ارسال خواهد شد"
        is_sended="not ok" #for handeling panel page button`s

        if request.method == 'POST':
            text=request.POST.get("textbox")
            if text:
                a=energy_sender(numbers,text)
                b=need_charge(need_charge_numbers)
                if a!="error":
                    actives.update(charge=F("charge")-1) #update member charges to charge=charge-1
                    messege="پیام شما با موفقیت برای همه ارسال شد"
                    is_sended="ok"#for handeling panel page button`s
                else:
                    messege = "متاسفانه پیام ارسال نشد.از لاگ برنامه خطارو بررسی کنید"
                    return render(request,'panel.html',{"messege":messege,"is_sended":is_sended})
            else:
                messege="<br>نمیتوانید متن خالی به کاربران ارسال کنید!!! <br><br>"
    else:
        return redirect("/")
    return render(request,'panel.html',{"messege":messege,"is_sended":is_sended})