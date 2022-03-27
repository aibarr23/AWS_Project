#from socket import *
import socket
import time
from datetime import datetime

address = ('127.0.0.1', 5000) #define server IP and port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #set op the socket
client_socket.settimeout(1) # Only wait 1 second for a response
   
# this will send the information to the arduino(Controller) via UDP cient
# function variables format=> (Temperature);(Feels Like(temp));(Air pressure);(Humidity);(Wind direction);(Wind speed);(cloud percentage);(Precipitation(of the recent or near hour))
# Currently only sending most needed Temperature, temp feals like, and precipitation
def SendW_toCtr(T, Tfl, Pre):
    
    data = "WData" + ";" + T + ";" + Tfl + ";" + Pre# ";" + Ap + ";" + H + ";" + Wd + ";" + Ws + + ";" + Cp

    while(1):
        
        client_socket.sendto(data.encode(), address)

        try:

            rec_data, addr = client_socket.recvfrom(2048) # read response from arduino
            #res = float(rec_data) #Convert string rec_data to float res(response)
            print("Received response from:"+ addr)
            print (rec_data)#print the result
        except:
            print("Request timed out, could not send")
            break
            #pass
        
        time.sleep(2) #delay befor sending next command
        


# this loop will check for possible recieved packets
def store_Data(self):
    
    try:
        R_data, addr = client_socket.recvfrom(1024) # read response
        time_recv = datetime.now()
        
        # get data and store it in text file for future analysis
        if(R_data[0].decode().size() > 0):
            
            data_R = R_data[0].decode()
            data = time_recv + ": " + data_R + "\n"
            
            #send data to app to update here
            
            text_file = open("data.txt", "a")
            text_file.write(data)
            text_file.close()
    except:
        pass
