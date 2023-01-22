        
from main import *


# Fixed parameters
# v_mag sets the speed of all three snails.
# scale sets the side length of the triangle.
v_mag = 5
scale = 20

#Initialize the three snails.
A = Snail(r = np.array([0.5*scale,0,0]),vel=np.array([0,0,0]),m=1)
B = Snail(r = np.array([-0.5*scale,0,0]),vel=np.array([0,0,0]),m=1)
C = Snail(r = np.array([0,np.sqrt(0.75)*scale,0]),vel=np.array([0,0,0]),m=1)

#Create arrays to save positions.
pos_A_x = []
pos_A_y = []

pos_B_x = []
pos_B_y = []
 
pos_C_x = []
pos_C_y = []

#Loop over small time steps to incriment positions and (direction of) velocity.
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


# Arrays to draw triangle.
x_1 = np.arange(-scale*0.5,scale*0.5,0.001)
x_2 = np.arange(-scale*0.5,0,0.001)
x_3 = np.arange(0,scale*0.5,0.001)

# Plot output.
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
plt.savefig("spiral_solution")
plt.show()

