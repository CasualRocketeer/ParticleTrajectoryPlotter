import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation

e=2.714
pi=3.14
def cos(x):
    return math.cos(x)


def sin(x):
    return math.sin(x)


def tan(x):
    return math.tan(x)


def fun_control(c):
    con = False
    while con == False:
        xyz_fun = input("\nUnesi funkciju za {} koordinate: {}(t)=".format(c, c))
        try:
            t = 1
            eval(xyz_fun)
            con = True
        except SyntaxError:
            print("Kriva sintaksa, napisite funkciju ponovno: ")
        except NameError:
            print("Krivi input, napisite funkciju ponovno:")
    return xyz_fun

def update(i):
        trajectory.set_data(x_cord[:i],y_cord[:i])
        trajectory.set_3d_properties(z_cord[:i])
        return trajectory

if __name__ == "__main__":
    print("_____Program_za_plotiranje_putanje_____"
          "\nUnesite x,y,z putanju kao funkciju vremena:")

    x_fun = fun_control("x")
    y_fun = fun_control("y")
    z_fun = fun_control("z")
    t= int(input("UNESI VRIJEME TRAJANJA PUTANJE(s): "))
    t_increment=float(input("UNESITE FINOCU PUTANJE:"))
    frames_t=int(t/t_increment)
    t_max = max([eval(x_fun), eval(y_fun), eval(z_fun)])
    x_cord=[]
    y_cord=[]
    z_cord=[]
    for i in np.arange(0,t,t_increment):
        t=i
        x_cord.append(eval(x_fun))
        y_cord.append(eval(y_fun))
        z_cord.append(eval(z_fun))
    x_cord = np.array(x_cord)
    y_cord = np.array(y_cord)
    z_cord=np.array(z_cord)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    trajectory, = ax.plot(0,0,0)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, t_max)
    ax.set_zlim(0, t_max)
    ani =animation.FuncAnimation(fig, update,frames_t, interval=25*(t-1)/((t/t_increment)-1))

    plt.show()
