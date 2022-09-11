from flask import request
import ipStack

'''
Author: Bryan Ison
Date: 2/18/2021

Description:
Calls up the IP stack to deliver json data to the frontend.
'''


# ALL SERVICE ENDPOINTS STAY HERE IN API
def get_data():
    print("Getting ip data....")
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        payload = request.environ['REMOTE_ADDR']
    else:
        payload = request.environ['HTTP_X_FORWARDED_FOR']  # if behind a proxy

    print(payload)
    data = ipStack.IpStack(payload)
    payload = data.getData()

    # finally open the map while returning payload
    # load_map(data.latitude, data.longitude)
    print("PayLoad: " + str(payload))
    return payload, data


def get_payload():
    print("Getting ip....")
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        payload = request.environ['REMOTE_ADDR']
    else:
        payload = request.environ['HTTP_X_FORWARDED_FOR']  # if behind a proxy

    # finally open the map while returning payload
    # load_map(data.latitude, data.longitude)
    print("PayLoad: " + str(payload))
    return payload
