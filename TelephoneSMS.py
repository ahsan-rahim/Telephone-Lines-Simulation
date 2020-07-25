# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:01:56 2020

@author: Ahsan Rahim
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:09:26 2020

@author: Ahsan Rahim
"""

import matplotlib.pyplot as plt
import numpy as np
from random import choice


#All time units are in seconds

#Creating a normal distribution for inter call arrival time from A to B
# mean=10 , std=5 , size=100
iatAB = np.random.normal(10, 5, 100)
iatAB= np.abs(iatAB.astype(int))

#Creating a normal distribution for inter call arrival time from B to A
# mean=12 , std=5 , size=100
iatBA = np.random.normal(12, 5, 100)
iatBA= np.abs(iatBA.astype(int))



#Creating a normal distribution for call lengths.
# mean= 4 mins  , std= 3 mins
callLength = np.random.normal(4*60, 3*60 , 100)
callLength=np.abs(callLength.astype(int))


twelveHours = 12*60*60






#Initializing variables
cList=[]
dList=[]
percentageDroppedCalls=[]
dropPercentage=100
k=0



#Simulation starts
while(dropPercentage>0.00):
    
    #Initializing empty lines where K represents the number of lines    
    lines=[0]*k     
    
    connected=0
    dropped=0
    
    #Selecting a random value from the inter call arrival pools for both A to B and B to A
    nextAB=choice(iatAB)
    nextBA=choice(iatBA)
    simTime=min(nextAB,nextBA)
    
    while(simTime<twelveHours):
       
        #Calculating available free lines
       freeLines= [i for i in lines if i<= simTime]
         
       #If a call is made from both A to B and B to A at the same time
       if(nextAB==nextBA):
           #Update values
           simTime+=nextAB
           nextAB=choice(iatAB)
           nextBA=choice(iatBA)
           
           #Assign both incoming calls to a free line if available otherwise drop the call and increase counters accordingly
           for m in range(2):
                   
              if( len(freeLines)!=0): 
                 lines[lines.index(freeLines.pop(0))]=simTime+choice(callLength)
                 connected+=1
              else:
                   dropped+=1
                   
               
       else:
           #Assign the sole incoming call to a free line if available otherwise drop the call and increase counters accordingly
           if( len(freeLines)!=0):    
             lines[lines.index(freeLines.pop(0))]=simTime+choice(callLength)
             connected+=1
           else:
               dropped+=1
               
           
           #update values next call arrival times and simulation time accordingly. 
           if(nextAB>nextBA):
               simTime+=nextBA
               nextAB=nextAB-nextBA
               nextBA=choice(iatBA)
               
           else:
               simTime+=nextAB
               nextBA=nextBA-nextAB
               nextAB=choice(iatAB)
    
    #Calculate drop percentage  and append to a list (dList) for each iteration to generate a graph later.
    dropPercentage=dropped/(connected+dropped)           
    cList.append(connected)
    dList.append(dropped)
    percentageDroppedCalls.append(dropPercentage)
    
    #Print out connected, dropped and total calls as well as dropped percentage
    print("\nLines = "+ str(k))
    print("Calls connected = " , connected)
    print("Calls dropped = " , dropped) 
    print("Total Calls = " , connected+dropped)      
    print("Percentage of Dropped Calls = " + str(dropPercentage))
    k+=1
    
    


#Plot out the graph showing the relationship between number of lines and drop percentage.
     
line=range(1,k+1)
plt.plot(line, percentageDroppedCalls) 
  
# naming the x axis 
plt.xlabel('Number of Lines') 

# naming the y axis 
plt.ylabel('Percentage Calls Dropped') 

# giving a title to the graph 
plt.title('Lines vs % Dropped Calls')
 
# function to show the plot 
plt.show()      