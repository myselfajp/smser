from ippanel import Client, Error, HTTPError, ResponseCode


client = Client("aS6I_1xffDVb4NpSaTb66ihtUKqJaoPy8nZYLuEpdfY=")

def energy_sender(numbers,text):
    try:
        bulk_id = client.send("+983000505",numbers, text)
        return bulk_id

    except Error as e:
        print("Error handled => code: %s, message: %s" % (e.code, e.message))

        if e.code == ResponseCode.ErrUnprocessableEntity.value:
            for field in e.message:
                print("Field: %s , Errors: %s" % (field, e.message[field]))
        return "error"
    except HTTPError as e:
        print("Error handled => code: %s" % (e))
        return "error"






def need_charge(numbers):
    text="همراه گرامی برموداانرژی یک روز دیگه به پایان اشتراک شما باقی مانده است، لطفا در صورت تمایل جهت تمدید اشتراک اقدام کنید"
    try:
        bulk_id = client.send("+983000505",numbers, text)
        return bulk_id

    except Error as e:
        print("Error handled => code: %s, message: %s" % (e.code, e.message))

        if e.code == ResponseCode.ErrUnprocessableEntity.value:
            for field in e.message:
                print("Field: %s , Errors: %s" % (field, e.message[field]))
        return "error"
    except HTTPError as e:
        print("Error handled => code: %s" % (e))
        return "error"
