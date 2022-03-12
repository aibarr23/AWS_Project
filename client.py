from socket import *
import time

address = ('10.1.15.243', 5000) #define server IP and port
client_socket = socket.socket(socket.AF_INET, SOCK_DGRAM) #set op the socket
client_socket.settimeout(1) # Only wait 1 second for a response

while(1):

    data = "Temperature" #set data request to temperature
    
    client_socket.sendto(data, address) #Send the data request

    try:

        rec_data, addr = client_socket.recvfrom(2048) # read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print ("The Measured Temperature is ", temp, "degreeF.")#print the result
    except:
        pass
    
    time.sleep(2) #delay befor sending next command
    

