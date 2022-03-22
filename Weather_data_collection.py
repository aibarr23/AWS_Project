# import pyowm

#libraries to use
from pyowm.commons import exceptions
from pyowm.utils import formatting, measurables, timestamps
from pyowm.weatherapi25.uris import ICONS_BASE_URI
from pyowm.owm import OWM

def get_weather():
    # global formattedktof,formattedktof_feelslike, formattedmbtoinhg, humidity, x, formattedkmhr, clouds, z
    #gathering data from apikey
    owm=OWM('d4adacdab2c752357183aaafdb017bbb')                  
    mgr = owm.weather_manager()
    Weather = mgr.weather_at_place("Chicago")
    Data = Weather.weather
   
    #gathering data and printing result
    temp=Data.temp
    pressure=Data.pressure
    humidity=Data.humidity
    clouds=Data.clouds
    wind=Data.wnd
    rain=Data.rain

    #converting to km/hr for wind(originally in meters/sec)
    convertkmhr=(wind['speed']*3.6)

    #converting to fahrenheit for temp
    convertktof=(temp['temp']-273.15)*(9/5)+32
    convertktof_feelslike=(temp['feels_like']-273.15)*(9/5)+32

    #converting to inches of mercury for pressure
    convertmbtoinhg=(pressure['press']/33.864)

    #formatting values to one decimal place
    formattedktof="{:.1f}".format(convertktof)
    formattedktof_feelslike="{:.1f}".format(convertktof_feelslike)
    formattedmbtoinhg="{:.2f}".format(convertmbtoinhg)
    formattedkmhr="{:.1f}".format(convertkmhr)

    #determining wind direction
    if wind['deg']>=30 and wind['deg']<=60:
        x=("NE")
    if wind['deg']>60 and wind['deg']<120:
        x=("E")
    if wind['deg']>=120 and wind['deg']<=150:
        x=("SE")
    if wind['deg']>150 and wind['deg']<210:
        x=("S")
    if wind['deg']>=210 and wind['deg']<=240:
        x=("SW")
    if wind['deg']>240 and wind['deg']<300:
        x=("W")
    if wind['deg']>=300 and wind['deg']<=330:
        x=("NW")
    else:
        x=("N")

    #printing out all the data
    print(f"Temperature: {formattedktof}F")
    print(f"Feels like: {formattedktof_feelslike}F")
    print(f"Pressure: {formattedmbtoinhg}inHg") 
    print(f"Humidity: {humidity}%")
    print(f"Wind conditions: {x} winds at {formattedkmhr}km/hr")
    print(f"Cloud cover: {clouds}%")
    print("\n")


    '''
    Web scraping starts here. 
    It is separate from the openweathermap api data.
    '''
    from requests_html import HTMLSession, HTML

    session = HTMLSession()

    #url where precip percentage is gathered from
    url = f'https://weather.com/en-IN/weather/hourbyhour/l/e0abde3003a88dedecad92fedc96375000c16843287a51dbf2cd92f062217180'

    r = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'})

    #code searches here for precip in website
    # divs = r.html.find('div.DetailsSummary--DetailsSummary--2HluQ')
    # rats = r.html.find('div.DetailsSummary--precip--1ecIJ')

    #this count is for how many hours you want to gather precip chance data for
    #initialized at 0 hours
    

    
    x1 = r.html.find('div.DetailsSummary--DetailsSummary--2HluQ h2.DetailsSummary--daypartName--2FBp2', first=True).text
    print(x1)
    y1 = r.html.find('div.DetailsSummary--precip--1ecIJ span', first=True).text   
    print(y1)
    print("\n")
    z = x1+"\n"+y1

    return rain, formattedktof,formattedktof_feelslike, formattedmbtoinhg, humidity, x, formattedkmhr, clouds, z

#all this code below is where the rain measurement web scraping goes
#Ping tom park is closest weather gauge to campus. ~1.25mi from campus
def get_precipitation(location:str, hrs:list):
    import requests
    url = "https://il.water.usgs.gov/gmaps/precip/data/rainfall_outIL_WSr2.json"
    r = requests.get('https://il.water.usgs.gov/gmaps/precip/data/rainfall_outIL_WSr2.json').json()
   
    #searching for data in json file
    data = [i for i in r['value']['items'] if i['title'] == location][0] 
    
    #printing out data gathered from json file
    for k,v in data.items():
        if k in hrs:
            print(f'{k}={v}') #all values in inches


    if __name__ == "__main__":
    
        location = "RAIN GAGE AT PING TOM PARK AT CHICAGO, IL"   #Do not change this line. This is for the location
        hrs = ['precip1hrvalue', 'precip3hrvalue', 'precip6hrvalue', 'precip12hrvalue'] #change hourly values here

        get_precipitation(location, hrs)
