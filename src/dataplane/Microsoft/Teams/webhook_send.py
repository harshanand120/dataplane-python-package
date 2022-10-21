import requests
import os
from datetime import datetime
import json

""" Url: Webhook url generated by Teams
Message: Json message to send
ProxyUse: Whether to use a proxy, true or false
ProxyUrl: Proxy endpoint to use
ProxyMethod: https or http, default https
"""
def TeamsWebhookSend(Url, Message, ProxyUse=False, ProxyUrl="", ProxyMethod="https"):

    # Start the timer
    start  = datetime.now()

    headers = {
        "Content-Type": "application/json"
    }
    
    if ProxyUse==True:
        proxies = {ProxyMethod: ProxyUrl}
    else:
        proxies = {}

    r = requests.request("POST", Url, headers=headers, json=Message, proxies=proxies)
    
    if r.status_code != 200:
        duration = datetime.now() - start
        return {"result":"Fail", "reason":"Webhook fail", "duration": str(duration), "status": r.status_code, "error": r.json()} 
    duration = datetime.now() - start

    return {"result":"OK", "duration": str(duration), "status": r.status_code, "response": r.json()} 