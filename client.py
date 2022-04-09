import socket
import time
from datetime import datetime

address = ('10.0.0.56', 2390) #define server IP and port
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



# this will send notify the controller that it has control again
def Return_control():
    data = "Rcntr;"# Rcntr stands for Return control
    while(1):
        client_socket.sendto(data.encode(), address)

        try:

            rec_data, addr = client_socket.recvfrom(2048) # read response from arduino
            #res = float(rec_data) #Convert string rec_data to float res(response)
            print("Received response from:"+ addr)
            print (rec_data)#print the result
            x = "accepted"
            return rec_data.decode(), str(x)
        except:
            print("Request timed out, could not send")
            return "rejected", "denide"
        




# this will close all solenoids
# so: stands for solenoid-> 0: all solenoids; 1: solenoid 1, etc.
# action: c: close; o: open
def CLASo(so, action):
    
    data = "CalSo;"# refers to clos all solenoids
    
    while(1):
        client_socket.sendto(data.encode(), address)

        try:

            rec_data, addr = client_socket.recvfrom(2048) # read response from arduino
            #res = float(rec_data) #Convert string rec_data to float res(response)
            print("Received response from:"+ addr)
            print (rec_data)#print the result
            x = "success"
            return str(x)
        except:
            print("Request timed out, could not send")
            return "denide"



# this loop will check for possible recieved packets
def store_Data(self):
    
    data = "SData"
    
    # client_socket.sendto(data.encode(), address)
    try:
        R_data, addr = client_socket.recvfrom(1024) # read response
        time_recv = datetime.now()
        
        # test store data function
        print(R_data.decode())
        print(time_recv)
        
        # get data and store it in text file for future analysis
        S_data(R_data)
        
    except:
        pass
    

# this is the function that will store the data into a file
def S_data(R_data):
    
    sD = ""
    time_recv = datetime.now()
    
    if(type(R_data) == bytes):
        sD = str(R_data.decode())
    else:
        sD = R_data
        
    if(len(sD) > 0):
            
        data = time_recv.strftime(" %d/%m/%Y %H:%M:%S\n") + ": " + sD + "\n"
        
        #send data to app to update here
        
        text_file = open("data.txt", "a")
        text_file.write(data)
        text_file.close()
