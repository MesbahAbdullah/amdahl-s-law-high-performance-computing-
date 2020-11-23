from matplotlib import pyplot as plt
import math
import numpy as np

fig, ax = plt.subplots()
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 23:52:21 2020

@author: Mosbah
"""


ax.set_ylabel("Speedup")
ax.set_xlabel("rBCEs")
 
system=input("enter your  system symmetric press 1 for Asymmetric press 2 for dynamic press 3 :  ")
while(True):
 f1=float(input("enter your software fraction          f  "))
 n1=int  (input("enter your rescource budget in BCES   n  "))
 x_R=[]
 y_speed=[]
 xAxis=[]
 x_R1=[]
 xSteps=n1
 for j in range(0,n1):
    if xSteps<1:
        break
    x_R1.insert(j, xSteps)
    xSteps=int(xSteps/2)
    

 xAxis=x_R1.copy()
 xAxis.reverse()
 xAxis.insert(0, 0)
 xAxis.pop(1)
 rBCEs=xAxis.copy()
 rBCEs.pop(0)
 rBCEs.insert(0, 1)
 
 speedup=np.array([])
 
 if system=="1":
      for  i in range(1,n1+1):          
          x_R.append(i)
          perf_r1=math.sqrt(i)          
          y_speed.append(round((1/(((1-f1)/perf_r1) +((f1*i)/(perf_r1*n1)))),1))
          if i<=len(rBCEs):
           perf_r1=math.sqrt(rBCEs[i-1])           
           speedup=np.append(speedup,((1/(((1-f1)/perf_r1) +((f1*rBCEs[i-1])/(perf_r1*n1)))),1))
   
 elif system=="2":
    for  i in range(1,n1+1):          
          x_R.append(i)
          perf_r1=math.sqrt(i)          
          y_speed.append(round((1/(((1-f1)/perf_r1) +((f1)/(perf_r1+n1-i)))),1))
          if i<=len(rBCEs):
           perf_r1=math.sqrt(rBCEs[i-1])          
           speedup=np.append(speedup,((1/(((1-f1)/perf_r1) +((f1)/(perf_r1+n1-rBCEs[i-1])))),1))

 elif system=="3":
    for  i in range(1,n1+1):          
          x_R.append(i)
          perf_r1=math.sqrt(i)          
          y_speed.append(round((1/(((1-f1)/perf_r1) +((f1)/(n1)))),1))
          if i<=len(rBCEs):
            perf_r1=math.sqrt(rBCEs[i-1])          
            speedup=np.append(speedup,(((1/(((1-f1)/perf_r1) +((f1)/(n1)))),1)))

 plt.grid(True)
 plt.ylim(1,n1,2)
 ax.set_xscale('log', basex=2)
 ax.set_xticks(rBCEs)
 ax.set_xticklabels(rBCEs)
 plt.plot(x_R,y_speed,color='red') 
 print("the best speedup =  %0.2f " % np.amax(speedup))
