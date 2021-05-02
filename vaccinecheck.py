import requests
import json
import time

xURL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?"

for i in range(1,1000,1):
    print(i)
    r = requests.get(url = xURL, params = {"district_id" :"363", "date" : "03-05-2021"})
    data = r.json()   
    centerList = data["centers"]
    for center in centerList: 
        sessionList  = center["sessions"]    
        for session in sessionList:
            if(session["min_age_limit"] == 18 and session["available_capacity"] > 0 ):
                print(center["name"], center["block_name"],center["pincode"], session["date"], session["available_capacity"] )                
            
                
    time.sleep(60)        
    i=i+1