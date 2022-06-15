# Program: MFI3D
# Authors: Rocha21
# Description: Plots the MFI on the 3d Earth's model
# Resource: https://stevendkay.wordpress.com/2009/10/12/scatter-plots-with-basemap-and-matplotlib/

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm

data = pd.read_csv('000 expanded_Node2_Izzy_astro_pi_datalog PARA MAPA.csv', delimiter='\t')

x=data.loc[:,'LON'].values
y=data.loc[:,'LAT'].values
z=data.loc[:,'mfi'].values

# From Canary Islands
m = Basemap(projection='ortho', lat_0=28, lon_0=-15, resolution='l')

# From Equator
# m = Basemap(projection='ortho', lat_0=0, lon_0=60, resolution='l')

#m = Basemap(projection='ortho', lat_0=0, lon_0=165, resolution='l')


m.drawcoastlines()
m.drawcountries()

x1,y1=m(x,y)

m.scatter(x1,y1,c=z,s=2,cmap=cm.jet,alpha=0.7,vmin=np.min(z), vmax=np.max(z))

plt.title("MFI 3D")
plt.show()

