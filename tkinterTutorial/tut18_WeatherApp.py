'''
Created on Mar 9, 2020

@author: marbe
'''
from tkinter import *
from PIL import ImageTk, Image
import requests         # pip install requests
import json

root = Tk()
root.title("Wetaher app")
root.iconbitmap('suez_logo.ico')
root.geometry("600x100")


# Create Zipcode lookup
def zipLookup():  
    #zip.get()
    #zipLabel = Label(root, text=zip.get())
    #zipLabel.grid(row=1,column=0,columnspan=2)

    # http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=FCC2A60D-B0AC-4FCD-BEB1-AC1EBC6F5010

    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=FCC2A60D-B0AC-4FCD-BEB1-AC1EBC6F5010")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#FF9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"
    
        root.configure(background=weather_color)
    
        myLabel = Label(root,text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica",20), background=weather_color)
        myLabel.grid(row=1,column=0,columnspan=2)

    except Exception as e:
        api = "Error..."


zip = Entry(root)
zip.grid(row=0,column=0,stick = W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command = zipLookup)
zipButton.grid(row=0,column=1,stick = W+E+N+S)

root.mainloop()