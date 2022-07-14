from tokenize import Name
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import  Http404
from django.urls import reverse
from .defs import congratulate
from .models import paymented
import logging

@login_required
def go_to_gateway_view(request):
    user=request.user
    number=user.phone_number
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 215000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = number  # اختیاری

    try:
        factory = bankfactories.BankFactory()
        try:
            bank = factory.auto_create('ZARINPAL') # or factory.create(bank_models.BankType.BMI) or set identifier
            bank.set_request(request)
            bank.set_amount(amount)
            # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
            bank.set_client_callback_url(reverse('callback'))
            bank.set_mobile_number(user_mobile_number)  # اختیاری
        
            # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
            # پرداخت برقرار کنید. 
            bank_record = bank.ready()
            
            # هدایت کاربر به درگاه بانک
            return bank.redirect_gateway()
        except AZBankGatewaysException as e:
            logging.critical(e)
            # TODO: redirect to failed page.
            raise e

    except:
        name=user.first_name
        charge=user.charge
        error="مشکل در اتصال به درگاه پرداخت . لطفا دوباره امتحان کنید"
        return render(request,'profile.html',{"name":name,"charge":charge,"error":error})
        




@login_required
def callback_gateway_view(request):
    
    user=request.user
    name=user.first_name
    number=name
    charge=user.charge
    if name:
        name=f"{name} عزیز سلام"
    else:
        name="دوست عزیز سلام"

    try:
        tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
        if not tracking_code:
            logging.debug("این لینک معتبر نیست.")
            raise Http404

        try:
            bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
        except bank_models.Bank.DoesNotExist:
            logging.debug("این لینک معتبر نیست.")
            raise Http404

    except:
        error="پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت."
        return render(request,'profile.html',{"name":name,"charge":charge,"error":error})


    if bank_record.is_success:
        tc=request.GET.get("tc")
        try:
            check=paymented.objects.get(ok=tc)
        except:
            check=None

        if not check:
            error="پرداخت با موفقیت انجام شد"
            user.charge=user.charge+30
            user.save()
            charge=user.charge
            check=paymented()
            check.ok=tc
            check.user=user
            check.save()
            # congratulate(number) #need active
        else:
            error="این کد تایید پرداخت منقضی شده است.اگر پول کم شده است به پشتیبانی پیام دهید"
        return render(request,'profile.html',{"name":name,"charge":charge,"error":error})

    error="پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت."
    return render(request,'profile.html',{"name":name,"charge":charge,"error":error})
