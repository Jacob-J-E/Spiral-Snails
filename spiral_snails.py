import numpy as np
import matplotlib.pyplot as plt



class Snail:

    def __init__(self,r=np.array([0,0]),v=np.array([0,0]),m=1):
        self.r = np.array(r).astype(float)
        self.vel = np.array(v).astype(float)
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
    

def gen_unit_vector(vector):
     mag = np.sqrt(np.dot(vector,vector))
     return vector/mag
     

v_mag = 5
scale = 20
A = Snail(r = np.array([0.5*scale,0]),v=np.array([0,0]),m=1)
B = Snail(r = np.array([-0.5*scale,0]),v=np.array([0,0]),m=1)
C = Snail(r = np.array([0,np.sqrt(0.75)*scale]),v=np.array([0,0]),m=1)

CB_vec = C.get_pos() - B.get_pos()

# x_a = A.get_pos()
# x_b = B.get_pos()
# x_c = C.get_pos()

pos_A_x = []
pos_A_y = []

pos_B_x = []
pos_B_y = []
 
pos_C_x = []
pos_C_y = []



dt = 1e-6
for i in range(0,10000):
    r_AB = gen_unit_vector(B.get_pos() - A.get_pos())
    r_BC = gen_unit_vector(C.get_pos() - B.get_pos())
    r_AC = gen_unit_vector(A.get_pos() - C.get_pos())

    v_A = v_mag * r_AB
    v_B = v_mag * r_BC
    v_C = v_mag * r_AC

    A.set_vel(v_A)
    B.set_vel(v_B)
    C.set_vel(v_C)

    A.move(dt=0.01)
    B.move(dt=0.01)
    C.move(dt=0.01)

    X_a = A.get_pos()
    X_b = B.get_pos()
    X_c = C.get_pos()

    pos_A_x.append(X_a[0])
    pos_A_y.append(X_a[1])

    pos_B_x.append(X_b[0])
    pos_B_y.append(X_b[1])

    pos_C_x.append(X_c[0])
    pos_C_y.append(X_c[1])

x_1 = np.arange(-scale*0.5,scale*0.5,0.001)
x_2 = np.arange(-scale*0.5,0,0.001)
x_3 = np.arange(0,scale*0.5,0.001)

fig, ax = plt.subplots()
ax.scatter(pos_A_x,pos_A_y,color='red',label="Snail A")
ax.scatter(pos_B_x,pos_B_y,color='blue',label="Snail B")
ax.scatter(pos_C_x,pos_C_y,color='green',label="Snail C")

ax.plot(x_1,np.zeros_like(x_1),color="black",linewidth=5)
ax.plot(x_2,(np.sqrt(3)*x_2+scale*0.5*np.sqrt(3)),color='black',linewidth=5)
ax.plot(x_3,(-np.sqrt(3)*x_2),color='black',linewidth=5)

ax.legend(loc="upper right")
ax.set_xlabel("x-coordinate")
ax.set_ylabel("y-coordinate")

x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))
plt.show()



# plt.scatter(*x_a,color='red')
# plt.scatter(*x_b,color='red')
# plt.scatter(*x_c,color='red')

# plt.scatter(*X_a,color='blue')
# plt.scatter(*X_b,color='blue')
# plt.scatter(*X_c,color='blue')

# plt.show()
