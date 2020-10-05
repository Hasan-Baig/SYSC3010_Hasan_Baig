import http.client
import urllib.parse
import time

key = "54CDA6FJF4RCJ92C"
        
if __name__ == "__main__":
    #Write email address, project group and member identifier
    params = urllib.parse.urlencode({'field1': "hasanbaig@cmail.carleton.ca", 'field2': "L2-M-5",'field3': "a", 'key': key})
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("connection failed")