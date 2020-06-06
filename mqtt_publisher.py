import paho.mqtt.client as paho #mqtt library
import os
import json
import time
from datetime import datetime

#host name is localhost because both broker and python are Running on same 
#machine/Computer.
broker="localhost" #host name , Replace with your IP address.
topic="test";
port=1883 #MQTT data listening port
ACCESS_TOKEN='M7OFDCmemyKoi461BJ4j' #not manditory


def on_publish(client,userdata,result): #create function for callback
  print("published data is : ")
  pass

client1= paho.Client("control1") #create client object
client1.on_publish = on_publish #assign function to callback
client1.connect(broker,port,keepalive=60) #establishing connection
i = 0
#publishing after every 5 secs
while True:


  ret= client1.publish(topic,"%i" % i ) #topic name is test
  print(i)
  print("Please check data on your Subscriber Code \n")
  time.sleep(1)
  i += 1
  if i == 101: break

