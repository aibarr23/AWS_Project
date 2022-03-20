from socket import *
import time


# this will send the information to the arduino(Controller) via UDP cient
# function variables format=> (Temperature);(Feels Like(temp));(Air pressure);(Humidity);(Wind direction);(Wind speed);(cloud percentage);(Precipitation(of the recent or near hour))
# Currently only sending most needed Temperature, temp feals like, and precipitation
def SendW_toCtr(T, Tfl, Pre):
    
    address = ('10.1.15.243', 5000) #define server IP and port
    client_socket = socket.socket(socket.AF_INET, SOCK_DGRAM) #set op the socket
    client_socket.settimeout(1) # Only wait 1 second for a response
    data = "WData" + ";" + T + ";" + Tfl + ";" + Pre# ";" + Ap + ";" + H + ";" + Wd + ";" + Ws + + ";" + Cp

    while(1):
        
        client_socket.sendto(data, address)

        try:

            rec_data, addr = client_socket.recvfrom(2048) # read response from arduino
            res = float(rec_data) #Convert string rec_data to float res(response)
            print (res)#print the result
        except:
            pass
        
        time.sleep(2) #delay befor sending next command
        


