'''
Filename: main.py

Description:
    File is used for the Kivymd framework to run the aplications functionality
    
Author 1: Anthony Ibarra, 28aibarra@gmail.com
Author 2: Joe Biscan
    
Date: Spring 2022

'''
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog

from kivy.clock import Clock
from kivy.lang.builder import Builder
from helper import KV

# from Weather_data_collection import formattedktof, formattedktof_feelslike, formattedmbtoinhg, formattedkmhr, x, clouds
# from Weather_data_collection import humidity, z
from Weather_data_collection import get_weather
from client import SendW_toCtr, store_Data, S_data, Return_control, CLASo

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
def Show_Temp_Data(Tfl):
    # Tfl = "-.-"
    # Ttype = "Celsius" #getTempType_FC(desired_type)

    s = "\nFeels like: " + Tfl + "°"  + "  F"
    return  s

# this will show the data focused on water: for the precipitation, and humidity
def Show_Water_data(humidity, x1, y1):
    H = str(humidity)
    Per = x1+"\n"+y1
    s = "Precipitation:  " + Per  + "\n" + "Humidity:  " + H + "%"

    return s

# this function will show the data regarding the ambient
def Show_Air_data(Pr, Ws, x, Cl):

    s = "Pressure: " + Pr + " hPa" + "\n\n" + "Wind speed: " + Ws + " km/hr\n Wind direction: " + x + "\n\n" + "Cloud: " + str(Cl) + "%   "

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
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette= "BlueGray"
        self.theme_cls.primary_hue = "900"
        
        return Builder.load_string(KV)

    def on_start(self):
        
        # following statements will manage the solenoids by notigying arduino of changes
        
        pass

    # this is for the button to change the theme_style of the app from light too dark
    def theme_style(self, *args):
        def theme_style(interval):
            if self.theme_cls.theme_style == "Light":
                self.theme_cls.theme_style = "Dark"
            else:
                self.theme_cls.theme_style = "Light"
        Clock.schedule_once(theme_style, 1)


    # this function will return the control of the solenoids
    # from user to the microcontroller(arduino) to continue automation
    def Return_con(self, *args):
        def Return_con(interval):
            
            #return control
            self.root.ids.S1.disabled = False
            self.root.ids.S2.disabled = False
            self.root.ids.S3.disabled = False
            
            # obtain respones and data regarding solenoids state(rec_data)
            rec_data, response = Return_control()
            if(response == "accepted"):
                self.root.ids.S1.disabled = False
                self.root.ids.S2.disabled = False
                self.root.ids.S3.disabled = False
                # have controller take control of solenoids
                # here
        Clock.schedule_once(Return_con,1)


    # this function is for the use of the refresh button
    # will refresh the weather information every time it is pressed
    def refresh_weather(self,*args):
        def refresh_weather(interval):
            

            formattedktof,formattedktof_feelslike, formattedmbtoinhg, humidity, x, formattedkmhr, clouds, x1, y1 = get_weather()
            Current_City = "Weather Info for City: " + "Chicago"
            Tdata = Show_Temp_Data(formattedktof_feelslike)
            Wdata = Show_Water_data(humidity, x1, y1)
            Adata = Show_Air_data(formattedmbtoinhg, formattedkmhr, x, clouds)
            getDT = Get_Date_Time()
            T = formattedktof
            CTemp = "\n" + T + "°" + "  F" + "\n"

            self.root.ids.weatherheading.title = Current_City
            self.root.ids.datetime.text = getDT
            self.root.ids.cd1line1.text = CTemp
            self.root.ids.cd1line2.text = Tdata
            self.root.ids.mdc2.text = Wdata
            self.root.ids.mdc3.text = Adata
            
            # this will send the information to the arduino(Controller) via UDP cient
            # function variables format=> (Temperature);(Feels Like(temp));(Air pressure);(Humidity);(Wind direction);(Wind speed);(cloud percentage);(Precipitation(of the recent or near hour))
            # Currently only sending most needed Temperature, temp feals like, and precipitation
            SendW_toCtr(formattedktof,formattedktof_feelslike, y1 )

            # the function bellow will check the temperature
            # if the temperature is 20 degrees fahrenheit or bellow then the
            # user will get a notification regarding the pvc pipes
            if float(formattedktof_feelslike) <= 20:
                self.dialog = MDDialog(
                    title = "The temperature for today is bellow freezing point. Be sure to remove water from the system, If ambient temperature is bellow 20 F",
                    buttons = [
                        MDFlatButton(text = "Click outside of the box to return")
                    ]
                )
                self.dialog.open()
            

        # the following will runt the function once and run it again after given interval
        event = Clock.schedule_once(refresh_weather, 1)
        x = Clock.schedule_interval(event, 10)# the second input is for seconds
        event()
        
        if( args[0] == 's'):
            if(self.root.ids.AR.active== False):
                x()
                print("it is true now")
        else:
            x.cancel()
            Clock.unschedule(x)
            print("false")
    
    
    # function is called to close all solenoids that are open
    # and takes control from arduino to prevent overwriting
    def close_sol(self, *args):
        print(*args)
        
        # when args is 0 means to close all solenoids
        if(args[0] == '0'):
            # take control of all three solenoids
            
            # change the states of solenoids to close(LOW)
            print("should close all solenoids")
            resp = CLASo('0', '0')
            # get response that it was successful
            if(resp == "success"):
                self.root.ids.S1.active = False
                self.root.ids.S2.active = False
                self.root.ids.S3.active = False
        
        # when args is 1 means change solenoid 1 state
        elif(args[0] == '1'):
            
            # check solenoid current state then change it
            if(self.root.ids.S1.active == False):
                resp = CLASo('1', 'o')
                if(resp == "success"):
                    S_data("S1, closed")# store data
            else:
                resp = CLASo('1', 'c')
                if(resp == "success"):
                    S_data()
                    
        # when args is 2 means change solenoid 2 state
        elif(args[0] == '2'):
            
            # check solenoid current state then change it
            if self.root.ids.S2.active == False:
                resp = CLASo('2', 'o')
                if(resp == "success"):
                    store_Data()# store data
            else:
                resp = CLASo('2', 'c')
                if(resp == "success"):
                    store_Data()
                    
        # when args is 3 means change solenoid 3 state
        elif(args[0] == '3'):
            
            # check solenoid current state then change it
            if self.root.ids.S3.active == False:
                resp = CLASo('3', 'o')
                if(resp == "success"):
                    store_Data()# store data
            else:
                resp = CLASo('3', 'c')
                if(resp == "success"):
                    store_Data()
        
        
        


    # bellow this there will be variables used as functions inside the KV string that will
    # be used to build the apps main body
    #--------------------------------------

    # This will show the city the weather information is from
    formattedktof,formattedktof_feelslike, formattedmbtoinhg, humidity, x, formattedkmhr, clouds, x1, y1 = get_weather()
    Current_City = "Weather for City: " + "Chicago"
    Tdata = Show_Temp_Data(formattedktof_feelslike)
    Wdata = Show_Water_data(humidity, x1, y1)
    Adata = Show_Air_data(formattedmbtoinhg, formattedkmhr, x, clouds)
    getDT = Get_Date_Time()
    T = formattedktof
    CTemp = "\n" + T + "°" + "  F" + "\n"
    # End of variables used for functions
    #-----------------------------------
    Clock.schedule_interval(store_Data, 60)
    
    # this should check for incoming packets from the arduino server
    # regarding update for the UI
    # Clock.schedule_interval(())


AWSApp().run()
