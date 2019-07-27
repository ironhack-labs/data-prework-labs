#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os

try:
    os.chdir(os.path.join(os.getcwd(), "bus/.ipynb_checkpoints"))
    print(os.getcwd())
except:
    pass
#%% [markdown]
# # Bus
#
# This bus has a passenger entry and exit control system to monitor the number of occupants it carries and thus detect when there is too high a capacity.
#
# At each stop the entry and exit of passengers is represented by a tuple consisting of two integer numbers.
# ```
# bus_stop = (in, out)
# ```
# The succession of stops is represented by a list of these tuples.
# ```
# stops = [(in1, out1), (in2, out2), (in3, out3), (in4, out4)]
# ```
#
# ## Goals:
# * lists, tuples
# * while/for loops
# * minimum, maximum, length
# * average, standard deviation
#
# ## Tasks
# 1. Calculate the number of stops.
# 2. Assign to a variable a list whose elements are the number of passengers at each stop (in-out),
# 3. Find the maximum occupation of the bus.
# 4. Calculate the average occupation. And the standard deviation.
#

#%%
# variables
##def bus_stop (in,out)

# Each item depends on the previous item in the list + in - out.
pass_in = [2, 3, 5, 7]
pass_out = (1, 5, 7, 8)
max_pass = max(len(pass_in), len(pass_out))
print(max_pass)
print("hello")

#%%
# 1. Calculate the number of stops.
stops = []
i = 0
print(stops)

while i < max_pass:
    stops.append((pass_in[i], pass_out[i]))

print(stops)
print("hello")
#%%
# 2. Assign a variable a list whose elements are the number of passengers in each stop:


#%%
# 3. Find the maximum occupation of the bus.


#%%
# 4. Calculate the average occupation. And the standard deviation.

