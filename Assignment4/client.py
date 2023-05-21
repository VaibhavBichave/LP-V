# Python program imitating a client process

from timeit import default_timer as timer
from dateutil import parser
import threading
import datetime
import socket
import time

'''
Client thread function used to send time at client side 
'''

def startSendingTime(slave_client):
    
    while True:
        # Provide server with clock time at the client
        slave_client.send(str(datetime.datetime.now()).encode())
        print("Recent time sent successfully", end = "\n\n")
        time.sleep(5)
        

'''
Client Thread function used to receive synchronized time
'''

def startReceivingTime(slave_client):
    
    while True:
        # Receive data from the server
        Synchronized_time = parser.parse(slave_client.recv(1024).decode())
        print("Synchronized time at the client is: " + str(Synchronized_time), end = "\n\n")
        

        
'''
Function used to Synchronize client process time
'''
def initiateSlaveClient(port = 8080):
    slave_client = socket.socket()
    # Connect to the clock server on local computer
    slave_client.connect(('127.0.0.1', port))
    
    # Start sending time to server
    print("Starting to receive time from server\n")
    send_time_thread = threading.Thread(target = startSendingTime, args = (slave_client, ))
    send_time_thread.start()
    
    # Start receiving synchronized from server
    print("Starting to receiving synchronized time from server\n")
    receive_time_thread = threading.Thread(target = startReceivingTime, args = (slave_client, ))
    receive_time_thread.start()
    

# Driver function
if __name__=="__main__":
    # Initialize the slave/client
    initiateSlaveClient(port = 8080)
    
