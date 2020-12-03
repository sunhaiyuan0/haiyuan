#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


# # savgol_filter

# In[5]:


x = np.linspace(1,100,100)
y = np.random.randint(1,100,100)
y[50] = 300

y_smoothing = savgol_filter(y,13,9)
plt.xlabel("time")
plt.ylabel("counts")
plt.plot(x,y,label = "data")
plt.plot(x,y_smoothing,"r",linewidth = 1,label = "smoothing_data")
plt.legend()


# # make_interp_spline

# In[3]:


from scipy.interpolate import make_interp_spline


# In[4]:


x = np.linspace(1,200,100)
print(len(x))
y = np.random.randint(1,100,100)
print(len(y))
#x_smooth = np.linspace(x.min(), x.max(), 300)  # np.linspace 等差数列,从x.min()到x.max()生成300个数，便于后续插值
y_smooth = make_interp_spline(x, y)(x)
plt.plot(x, y_smooth,"r")
plt.plot(x,y,"b",linestyle=":")
plt.show()


# # convolve

# In[5]:


x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
yerr = np.random.random(100)*0.2
y = y + yerr
plt.plot(x,y)


# In[6]:


def convolve_smooth(data,h_size):
    H = np.ones(h_size)/h_size
    y_smooth = np.convolve(data,H,"same")
    return y_smooth


# In[11]:


y_fit = convolve_smooth(y,10)
plt.plot(x,y_fit,"r",lw = 3.5,label = "smooth")
plt.plot(x,y,"b",label = "data")
plt.legend()


# In[ ]:




