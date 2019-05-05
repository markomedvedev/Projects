import numpy as np
import pandas as pd
import numpy.linalg as la
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as mp


data=pd.read_csv(r'/Users/markomedvedev/Downloads/WRI130/exoplanet.csv')
# print(data)
planets=data[['mass','radius']].values
print(planets)
def filter(p):
    counter=0
    for i in range(0,len(p)):
        if (not np.isnan(p[i][0])) and (not np.isnan(p[i][1])):
            counter=counter+1
            print(counter)
    pl=np.zeros((counter,2))
    counter_1=0
    for i in range(0,len(p)):
          if (not np.isnan(p[i][0])) and (not np.isnan(p[i][1])):
              pl[counter_1][0]=p[i][0]
              pl[counter_1][1]=p[i][1]
              counter_1=counter_1+1
    return pl

planets_filter=filter(planets)
def gravity(p):
    gravity=np.zeros(len(p))
    for i in range(0,len(p)):
        gravity[i]=p[i][0]/(p[i][1]*p[i][1])*317.8/(11.2*11.2)
    return gravity
def take_ab(gravity,a,b):
    counter=0
    for i in range(0,len(gravity)):
        if gravity[i]>a and gravity[i]<b:
            counter=counter+1
    g=np.zeros(counter)
    counter_1=0
    for i in range(0,len(gravity)):
        if gravity[i]>a and gravity[i]<b:
            g[counter_1]=gravity[i]
            counter_1=counter_1+1
    return g
def plot_histogram(grav):
    n, bins, patches = mp.hist(grav,853,  histtype='step', cumulative=True)
    mp.grid(True,linestyle='-.',linewidth=0.5)
    mp.xlabel('gravity[G]')
    mp.title('Cumulative distribution of gravity of planets')
    mp.ylabel('number of planets')
    # mp.ylim(0, 1.05)
    mp.show()
g=gravity(planets_filter)
print(g)
plot_histogram(take_ab(g,0,8))
plot_histogram(g)
print(len(take_ab(g,0,200)))
