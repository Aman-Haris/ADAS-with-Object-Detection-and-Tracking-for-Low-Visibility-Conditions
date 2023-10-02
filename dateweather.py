from datetime import date
from datetime import datetime
import pyowm

def dttm():
 cd = str(date.today())
 t = datetime.now()
 ct = t.strftime("%H:%M:%S")
 return cd,ct

APIKEY='feb997d9860d9656bcf7e2006192a3b5'
OpenWMap=pyowm.OWM(APIKEY)                   
Weather=OpenWMap.weather_at_place('Bengaluru,IN')
Data=Weather.get_weather()

def temp():
                      
 temp = Data.get_temperature('celsius')
      
 return temp['temp']

def status():
    status = Data.get_status()
    return status

def detstatus():
    
    dstat = Data.get_detailed_status()
    print(dstat)
    return dstat

dttm()