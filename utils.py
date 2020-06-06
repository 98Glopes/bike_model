import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os

class State:

    def __init__(self, length=1.5, l_rear=0.75, max_angle=math.pi/12, dt=1e-3,
                                        x=0.0, y=0.0, yaw=0.0, v=0.0):
        
        #Physical characterists
        self.length = length # [m] vehicle length
        self.l_rear = l_rear # [m] distance from vehicle center of gravity to rear axis
        self.max_angle = max_angle # [rad] max steering angle

        #initial position states
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v
        self.rear_x = self.x - ((self.l_rear / 2) * math.cos(self.yaw))
        self.rear_y = self.y - ((self.l_rear / 2) * math.sin(self.yaw))

        self.dt = dt

    def update(self, v, delta):
        self.x += self.v * math.cos(self.yaw) * self.dt
        self.y += self.v * math.sin(self.yaw) * self.dt
        self.yaw += (self.v / self.l_rear * math.tan(delta)) * self.dt
        self.v = v
        self.rear_x = self.x - ((self.l_rear / 2) * math.cos(self.yaw))
        self.rear_y = self.y - ((self.l_rear / 2) * math.sin(self.yaw))
        self.delta = delta

    def calc_distance(self, point_x, point_y):
        dx = self.rear_x - point_x
        dy = self.rear_y - point_y
        return math.hypot(dx, dy)
    
    @property
    def query_state(self):
        """
        return a string in this format:
        X;Y;YAM;V;DELTA
        """
        return '%.3f;%.3f;%.3f;%.3f;%.3f' % (self.x, self.y, self.yaw, self.v, self.delta) 


class States:

    def __init__(self):
        self.x = []
        self.y = []
        self.yaw = []
        self.v = []
        self.t = []

    def append(self, t, state):
        self.x.append(state.x)
        self.y.append(state.y)
        self.yaw.append(state.yaw)
        self.v.append(state.v)
        self.t.append(t)


def ramp_signal(t, dx, initial=0, max=None):
    """
    Generate a ramp signal
    if max=None the return value tends to infinite
    """

    value = math.sin(t*dx) + initial
    if max == None:
        return value
    elif value > max:
        return max
    else:
        return value


def step(t, ofset):

    if t >= ofset:
        return 1
    else:
        return 0