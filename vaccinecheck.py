import requests
import json

xURL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?"


r = requests.get(url = xURL, params = {"district_id" :"363", "date" : "02-05-2021"})
data = r.json()   
centerList = data["centers"]
for center in centerList:
    if(center["pincode"]. )
    sessionList  = center["sessions"]
    
    for session in sessionList:
        if(session["min_age_limit"] == 45 and session["available_capacity"] > 0 ):
            print(center["name"], center["block_name"],center["pincode"], session["date"], session["available_capacity"] )
