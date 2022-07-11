import requests

def code_sender(number,code):
    api_key="Zgp9VyoykRnG4Uybdjd-J37wg6l9G7nXYhU64ffKXJM="
    p_id="jz4qss4jgr96bwg"
    link=f"http://ippanel.com:8080/?apikey={api_key}&pid={p_id}&fnum=3000505&tnum={number}&p1=verification-code&v1={code}"  

    result=requests.get(link)
    print(result.text)
