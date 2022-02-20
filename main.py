from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from helper import KV

from Weather_data_collection import formattedktof, formattedktof_feelslike, formattedmbtoinhg, formattedkmhr, x, clouds

class Tab(MDFloatLayout, MDTabsBase):
    pass
class Weather_tab(MDFloatLayout, MDTabsBase):
    pass
class system_tab(MDBoxLayout,MDTabsBase):
    pass
class plant_tab(MDBoxLayout, MDTabsBase):
    pass

class AWSApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Light"# "Dark" 
        self.theme_cls.primary_palette= "BlueGray"
        self.theme_cls.primary_hue = "900"


        # self.theme_cls.primary_accent_palette= "Teal"

        # self.theme_cls.secondary_palette= "Teal"
        # self.theme_cls.secondary_hue = "A200"

        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.tabs.add_widget(Weather_tab(icon="weather-sunny"))
        self.root.ids.tabs.add_widget(system_tab(icon="wrench"))
        self.root.ids.tabs.add_widget(plant_tab(icon="flower"))
        self.root.ids.tabs.add_widget(Tab(icon="flare"))

    # this will get the type of temperature from the weather data collection code
    # and choose the one that will be used    
    def getTempType_FC(type):
        if type == "Celsius":
            return "Celsius"
        else:
            return "Fahrenheit"    
    
    # this will show the data from the weather data collector
    def Show_Temp_Data():
        T = "-.-"
        Tfl = "-.-"
        Ttype = "Celsius" #getTempType_FC(desired_type)

        T = formattedktof
        Tfl = formattedktof_feelslike
        s = "\nTemperature: " + T + "°" + "    Feels like:" + Tfl + "°" 
        return  s
    

    # this will show the data focused on water: for the precipitation, and humidity
    def Show_Water_data():
        H = "-.-"
        Per = "-.-"

        s = "Precipitation:  " + Per + "%" + "\n" + "Humidity:  " + H + "%"

        return s

    # this function will show the data regarding the ambient 
    def Show_Air_data():
        Pr = str(formattedmbtoinhg)
        Ws = str(formattedkmhr)
        Cl = str(clouds)
        C_info = "--"

        s = "Pressure: " + Pr + " hPa" + "\n\n" + "Wind speed: " + Ws + " km/hr from: " + x + "\n\n" + "Cloud:" + Cl + "%   " + C_info

        return s

    # bellow this there will be variables used as functions inside the KV string that will
    # be used to build the apps main body
    #--------------------------------------

    # This will show the city the weather information is from
    Current_City = "Weather Info for City: " + "Chicago"
    Tdata = Show_Temp_Data()
    Pdata = Show_Water_data()
    Adata = Show_Air_data()
    T = formattedktof
    CTemp = "\n" + T + "°" + "  F" + "\n"
    variable_Z = 0
    # End of variables used for functions 
    #-----------------------------------

AWSApp().run()
