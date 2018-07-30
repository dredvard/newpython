# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:56:17 2018

@author: ekambulow
"""

import numpy as np

def create_arc(center_x,center_y,radius,theta0,theta,height_z):
    z = np.linspace(0, height_z, 2)
    theta = np.linspace(np.pi*2*theta0/360, np.pi*2*theta/360, 25)
    theta_grid, z_grid=np.meshgrid(theta, z)
    x_grid = radius*np.cos(theta_grid) + center_x
    y_grid = radius*np.sin(theta_grid) + center_y
    return x_grid,y_grid,z_grid

def create_wall(center_x,center_y,radius,theta0,theta,height_z):
    xx, yy = np.meshgrid(range(10), range(10))
    z = np.linspace(0, height_z, 2)
    theta = np.linspace(np.pi*2*theta0/360, np.pi*2*theta/360, 25)
    theta_grid, z_grid=np.meshgrid(theta, z)
    wall=[(radius,theta,z),(radius,theta,0),(0,theta0,0),(0,theta,z)]
    wall0=[(radius,theta0,z),(radius,theta0,0),(0,theta0,0),(0,theta0,z)]
    x_grid = radius*np.cos(theta_grid) + center_x
    y_grid = radius*np.sin(theta_grid) + center_y
    return x_grid,y_grid,z_grid

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Xc,Yc,Zc = create_arc(0.2,0.2,0.05,0.1)
#ax.plot_surface(Xc, Yc, Zc, color='blue',alpha=1)
#ax.plot_surface(Xc, Yc, Zc, color='blue')
#ax.plot_surface(Xc, Yc, Zc, color='blue')

def draw_slice(theta0,theta,r,h,colors='b'):
    #cntr={x:0,y:0}
    Xc,Yc,Zc = create_arc(0,0,r,theta0,theta,h)
    ax.plot_surface(Xc, Yc, Zc, color=colors,linewidth=10, edgecolor='b')

draw_slice(0,90,1,1)
draw_slice(-90,0,1,1,'r')
draw_slice(90,270,1,1,'g')
    
plt.show()