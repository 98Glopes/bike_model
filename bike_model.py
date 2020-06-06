"""

Path tracking simulation with pure pursuit steering and PID speed control.

author: Atsushi Sakai (@Atsushi_twi)
        Guillaume Jacquenot (@Gjacquenot)

Classes State and States from PythonRobotics

"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import paho.mqtt.client as paho
import time

from utils import *


# Config mqtt broker parameters
broker="localhost" #host name , Replace with your IP address.
topic="simulation/status"
port=1883 #MQTT data listening port


if __name__ == "__main__":

    #config mqtt client
    client = paho.Client("control1") #create client object
    client.connect(broker,port,keepalive=60) #establishing connection
    #Config time variables
    total_time = 10*30 # max simulation time in seconds
    simulation_time = 0 #variable to increment during the simulation
    dt = 1e-3 # delta time

    # instance the bike model
    bike = State(dt=dt)

    # instance to save the bike states
    states = States()
    #start the simulation
    while simulation_time < total_time:

    
        v = 2
        delta = 0.13 * ramp_signal(simulation_time, 0.5, 0)

        bike.update(v, delta)
        states.append(simulation_time, bike)
        simulation_time += dt
        client.publish(topic, bike.query_state + ';%.3f' % simulation_time) #topic name is test
    #End of the simulation

    print('Tempo total de simulação: %i s' % simulation_time)
    print('Ultima posicao: x: %.2f m ; y: %.2f m' % (bike.x, bike.y))
    print('Numero de amostras da simulacao: %i' % len(states.y))
    plt.axis("equal")
    plt.grid(True)
    colors = cm.Reds(np.linspace(0, 1, len(states.x)))
    #plt.scatter(states.x, states.y, color=colors, s=2)
    #plt.show()

