from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.clock import Clock
from kivy.lang.builder import Builder
from helper import KV

# from Weather_data_collection import formattedktof, formattedktof_feelslike, formattedmbtoinhg, formattedkmhr, x, clouds
# from Weather_data_collection import humidity, z
from Weather_data_collection import get_weather

from datetime import datetime


class Tab(MDFloatLayout, MDTabsBase):
    pass
class Weather_tab(MDFloatLayout, MDTabsBase):
    pass
class system_tab(MDBoxLayout,MDTabsBase):
    pass
class plant_tab(MDBoxLayout, MDTabsBase):
    pass


# this will show the data from the weather data collector
def Show_Temp_Data():
    formattedktof,formattedktof_feelslike, formattedmbtoinhg, humidity, x, formattedkmhr, clouds, z = get_weather()
    T = "-.-"
    Tfl = "-.-"
    # Ttype = "Celsius" #getTempType_FC(desired_type)

    T = formattedktof
    Tfl = formattedktof_feelslike
    s = "\nFeels like: " + Tfl + "°"  + "  F"
    return  s

# this will show the data focused on water: for the precipitation, and humidity
def Show_Water_data():
    formattedktof,formattedktof_feelslike, formattedmbtoinhg, humidity, x, formattedkmhr, clouds, z = get_weather()
    H = str(humidity)
    Per = "-.-"

    s = "Precipitation:  " + Per + "%" + "\n" + "Humidity:  " + H + "%"

    return s

# this function will show the data regarding the ambient
def Show_Air_data():
    formattedktof,formattedktof_feelslike, formattedmbtoinhg, humidity, x, formattedkmhr, clouds, z = get_weather()
    Pr = formattedmbtoinhg
    Ws = formattedkmhr
    Cl = str(clouds)
    # C_info = "--"

    s = "Pressure: " + Pr + " hPa" + "\n\n" + "Wind speed: " + Ws + " km/hr\n Wind direction: " + x + "\n\n" + "Cloud: " + Cl + "%   "

    return s

# following function is for knowing the time and date this function was called
#
def Get_Date_Time():
    # datetime object containing current date and time
    now = datetime.now()
    # print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = " Date and Time weather was updated:" + now.strftime(" %d/%m/%Y %H:%M:%S\n")
    # print("date and time =", dt_string)
    return dt_string








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
        # self.root.ids.tabs.add_widget(Weather_tab(icon="weather-sunny"))
        # self.root.ids.tabs.add_widget(system_tab(icon="wrench"))
        # self.root.ids.tabs.add_widget(plant_tab(icon="flower"))
        # self.root.ids.tabs.add_widget(Tab(icon="flare"))
        pass



    # this function is for the use of the refresh button
    # will refresh the weather information every time it is pressed
    def refresh_weather(self, *args):
        def refresh_weather(interval):
            # self.root.ids.tabs.clear_widgets(Weather_tab)

            # print(self.root.ids)
            # self.root.ids.weabar.clear_widgets()
            # print(self.root.ids)
            # global Current_City
            # global Tdata
            # global Wdata
            # global Adata
            # global getDT
            formattedktof,formattedktof_feelslike, formattedmbtoinhg, humidity, x, formattedkmhr, clouds, z = get_weather()
            # get_weather()
            Current_City = "Weather Info for City: " + "Chicago"
            Tdata = "\nFeels like: " + formattedktof_feelslike + "°"  + "  F"
            Wdata = H = "Precipitation:  " + "%" + "\n" + "Humidity:  " + str(humidity) + "%"

            Adata = "Pressure: " + formattedmbtoinhg + " hPa" + "\n\n" + "Wind speed: " + formattedkmhr + " km/hr\n Wind direction: " + x + "\n\n" + "Cloud: " + str(clouds) + "%   "
            getDT = Get_Date_Time()
            T = formattedktof
            CTemp = "\n" + T + "°" + "  F" + "\n"

            print(Current_City)
            print(Tdata)
            print(Wdata)
            print(Adata)
            print(getDT)
            print(T)
            print(CTemp)


            self.root.ids.weatherheading.title = Current_City
            self.root.ids.datetime.text = getDT
            self.root.ids.cd1line1.text = CTemp
            self.root.ids.cd1line2.text = Tdata
            self.root.ids.mdc2.text = Wdata
            self.root.ids.mdc3.text = Adata

        Clock.schedule_once(refresh_weather, 1)

    # bellow this there will be variables used as functions inside the KV string that will
    # be used to build the apps main body
    #--------------------------------------

    # This will show the city the weather information is from
    # formattedktof,formattedktof_feelslike, formattedmbtoinhg, humidity, x, formattedkmhr, clouds, z = get_weather()
    # Current_City = "Weather Info for City: " + "Chicago"
    # Tdata = Show_Temp_Data()
    # Wdata = Show_Water_data()
    # Adata = Show_Air_data()
    # getDT = Get_Date_Time()
    # T = formattedktof
    # CTemp = "\n" + T + "°" + "  F" + "\n"
    # variable_Z = 0
    
    formattedktof,formattedktof_feelslike, formattedmbtoinhg, humidity, x, formattedkmhr, clouds, z = get_weather()
    # get_weather()
    Current_City = "Weather Info for City: " + "Chicago"
    Tdata = "\nFeels like: " + formattedktof_feelslike + "°"  + "  F"
    Wdata = H = "Precipitation:  " + "%" + "\n" + "Humidity:  " + str(humidity) + "%"

    Adata = "Pressure: " + formattedmbtoinhg + " hPa" + "\n\n" + "Wind speed: " + formattedkmhr + " km/hr\n Wind direction: " + x + "\n\n" + "Cloud: " + str(clouds) + "%   "
    getDT = Get_Date_Time()
    T = formattedktof
    CTemp = "\n" + T + "°" + "  F" + "\n"
    # W_refresh = refresh_weather()
    # End of variables used for functions
    #-----------------------------------

    

AWSApp().run()
