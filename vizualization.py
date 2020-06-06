import paho.mqtt.client as paho
import time
import sys
import datetime
import time
import collections

# MQTT configs
broker="localhost"  #host name
topic="simulation/status" #topic name

# Queue to save mqtt datha
global fila
fila = collections.deque([])

def on_message(client, userdata, message):

    fila.append(str(message.payload.decode("utf-8")))

client = paho.Client("user") #create client object 
client.on_message=on_message
print("connecting to broker host",broker)
client.connect(broker)#connection establishment with broker
print("subscribing begins here")    
client.subscribe(topic)#subscribe topic test
client.loop_start() #contineously checking for message  

class State:

    def __init__(self, query):

        self.query = query.split(';')
        self.x = float(self.query[0])
        self.y = float(self.query[1])
        self.yaw = float(self.query[2])
        self.v = float(self.query[3])
        self.delta = float(self.query[4])
        self.t = float(self.query[5])
        #print(self.t)

    def __str__(self):
        return 'x: %.2f y: %.2f yaw: %.2f v: %.2f delta: %.2f t: %.3f' % (self.x, self.y, self.yaw, self.v, self.delta, self.t )

    def __repr__(self):
        return self.__str__()

def main():
    # Time stick consirated in the video
    dt = 1 / 2
    # get the first simulate state
    while True:
    if len(fila) == 0:
        continue
    print('First state')
    print(last_state)        
    time.sleep(0.5)
    # start data vizualization

    while True:
        
        # if doesn't have an iten in the queue
        # the principal loop is skiped
        if len(fila) == 0: continue
        
        query = fila.popleft()
        atual_state = State(query)

        if atual_state.t > last_state.t + dt:
            print(atual_state.t)
            last_state = atual_state.copy()


if __name__ == '__main__':
    main()