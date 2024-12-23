
"""

Filename: Return_map_of_neuron.py
Name: Khang Ly 
Description: 
    This script runs the return map of neuron given a set of parameters 
    and initial conditions.

"""

import matplotlib.pyplot as plt 

# Set the value of parameters a, sigma (o), and meu (u) 
a = 18.7
o = 0.1
u = 0.25

X = []
Y = []

# Give x and y a value as the initial conditions

x = -1.2
y = -3.93

# Define a function to represent f(x,y)

def nonlinear_function(a,x,y):
    if x <= 0:
        return (a / (1-x)) + y
    elif x < (a+y):
        return (a+y)
    else:
        return -1 
   # return nonlinear_function 
   
# Create a for loop to get rid of the transient

for n in range(20000):      
    print(n,x,y)
    x1 = nonlinear_function(a, x, y)
    y1 = y - u*(x+1) + (u*o)
    
    x = x1
    y = y1
    
# Create another for loop to plot the map without the transient

for n in range(2000):
    print(n,x,y)
    x1 = nonlinear_function(a, x, y)
    y1 = y - u*(x+1) + (u*o)
    
    X.append(x1)
    Y.append(y1)
    
    x = x1
    y = y1

# Plot the map

fig, (ax1) = plt.subplots(1, 1, figsize=(16, 9))
                               #sharex=True)

ax1.plot(X,Y)
# Increase the size of tick labels on both x and y axes
plt.xticks(fontsize=25)  # Adjust the fontsize as needed
plt.yticks(fontsize=25)  # Adjust the fontsize as needed

# Adding labels and title
plt.xlabel('x', fontsize=25)  # Adjust the fontsize as needed
plt.ylabel('y', fontsize=25)  # Adjust the fontsize as needed
plt.title('Return map of neuron', fontsize=30)  # Adjust the fontsize as needed

plt.legend(fontsize = 25) # Adjust the fontsize as needed 

