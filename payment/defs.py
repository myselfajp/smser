import requests

def congratulate(number):
    api_key="Zgp9VyoykRnG4Uybdjd-J37wg6l9G7nXYhU64ffKXJM="
    p_id="er61slst6ohw0e7"
    link=f"http://ippanel.com:8080/?apikey={api_key}&pid={p_id}&fnum=3000505&tnum={number}"  

    result=requests.get(link)
    print(result.text)
