import numpy as np
import matplotlib.pyplot as plt

def gen_unit_vector(vector):
     mag = np.sqrt(np.dot(vector,vector))
     return vector/mag

class Snail:

    """
    Class to initialize snail object

    Attributes:
        - r is the position specified as a 2D vector numpy array.
        - vel is the velocity specified as a 2D vector numpy array.
        - m is the mass of the snail

    Methods:
        - get_pos() returns the position of the snail as a 2D numpy array.
        - get_vel() returns the velocity of the snail as a 2D numpy array.
        - get_mass() returns the mass of the snail.
        - set_pos(r) sets the position of the snail with input r, a 2D numpy array.
        - set_vel(v) sets the velocity of the snail with input v, a 2D numpy array.
        - momentum() returns magnitude of snail's momentum.
        - kinetic_energy() returns the kinetic energy of the snail.
        - move(dt) moves the snail by v*dt with float input dt. 
    """

    def __init__(self,r=np.array([0,0,0]),vel=np.array([0,0,0]),m=1):
        self.r = np.array(r).astype(float)
        self.vel = np.array(vel).astype(float)
        self.mass= float(m)

    def get_pos(self):
        return self.r
    
    def get_vel(self):
        return self.vel
    
    def get_mass(self):
        return self.mass
    
    def set_pos(self, r):
          self.r = np.array(r).astype(float)
    
    def set_vel(self, v):
          self.v = np.array(v).astype(float)

    def momentum(self):      
          return self.mass * np.sqrt(np.dot(self.vel,self.vel))
    
    def kinetic_energy(self):
          
          return 0.5 * self.mass * np.dot(self.vel,self.vel)
    
    def move(self,dt):
         
         self.r = self.r + self.v * dt
         return self
