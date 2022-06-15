# Script: plot_tat_lon_mfi colormap.py
# Description: Plot a 2d map of MFI
# Authors: Rocha21


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

fig = plt.figure()
ax1 = fig.add_subplot(111)

data = pd.read_csv('000 expanded_Node2_Izzy_astro_pi_datalog PARA MAPA.csv', delimiter='\t')

scatter=ax1.scatter(data.loc[:,'LON'],data.loc[:,'LAT'],c=data.loc[:,'mfi'],vmin=np.min(data.loc[:,'mfi']), vmax=np.max(data.loc[:,'mfi']),s=2,cmap=plt.cm.jet)

ax1.set_xlim(-185, 185)
ax1.set_ylim(-55, 55)

ax1.set_ylabel('Latitude (º)')
ax1.set_xlabel('Longitude (º)')

plt.colorbar(scatter)

ax1.set_title('Izzy MFI ', fontsize=14)
plt.show()


