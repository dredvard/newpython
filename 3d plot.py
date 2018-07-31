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


def pol2cart(radius,theta, units='deg'):
    if units=='deg':
        u=2*np.pi/360
    else:
        u=1
    x=radius*np.cos(u*theta)
    y=radius*np.sin(u*theta)
    return x,y

def create_wall(center_x,center_y,radius,theta,height_z):

    z = np.linspace(0, height_z, 2)
    r = np.linspace(0, radius, 10)
    r_grid, z_grid=np.meshgrid(r, z)
#    x_grid,y_grid = pol2cart(r_grid,theta+theta0) + (center_x,center_y)
    x_grid,y_grid = pol2cart(r_grid,theta)
    return x_grid+center_x,y_grid+center_y,z_grid

def create_lid(center_x,center_y,radius,theta0,theta,height_z):
    r = np.linspace(0, radius, 10)
    theta = np.linspace(np.pi*2*theta0/360, np.pi*2*theta/360, 25)
    theta_grid, r_grid,z_grid=np.meshgrid(theta, r, height_z)
    x_grid,y_grid = pol2cart(r_grid,theta_grid)
    return x_grid,y_grid,z_grid

from matplotlib.colors import LightSource
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
    ls = LightSource(azdeg=0, altdeg=65)
    # Shade data, creating an rgb array.
    Xc,Yc,Zc = create_arc(0,0,r,theta0,theta,h)
    rgb = ls.shade(Zc, plt.cm.RdYlBu)
    ax.plot_surface(Xc, Yc, Zc, 
                    rstride=1, cstride=1, 
                    antialiased=False,
                    color=colors,linewidth=1, edgecolor='b',facecolors=rgb)
    
    Xc,Yc,Zc = create_wall(0,0,r,theta0,h)
    rgb = ls.shade(Zc, plt.cm.RdYlBu)
    ax.plot_surface(Xc, Yc, Zc, 
                    rstride=1, cstride=1, 
                    antialiased=False,
                    color=colors,linewidth=1, edgecolor='b',facecolors=rgb)
    Xc,Yc,Zc = create_wall(0,0,r,theta0+theta,h)
    rgb = ls.shade(Zc, plt.cm.RdYlBu)
    ax.plot_surface(Xc, Yc, Zc, 
                    rstride=1, cstride=1, 
                    antialiased=False,
                    color=colors,linewidth=1, edgecolor='b',facecolors=rgb)
    Xc,Yc,Zc = create_lid(0,0,r,theta0,theta,h)
    #rgb = ls.shade(Xc, plt.cm.RdYlBu)
    ax.plot_surface(Xc, Yc, Zc, 
                    rstride=1, cstride=1, 
                    antialiased=False,
                    color=colors,linewidth=1, edgecolor='b',facecolors=rgb)
    
draw_slice(0,90,1,1)
#draw_slice(-90,0,1,1,'r')
#draw_slice(90,270,1,1,'g')

ax.set_axis_off()    
plt.show()