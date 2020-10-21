import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from Baseline import TD_baseline
from scipy import linalg as la
data = fits.open("glg_tte_n7_bn200919964_v00.fit")
x1 = np.sqrt(data[1].data.field(1)*data[1].data.field(2))
#print(x1)
t = data[2].data.field(0)
E = np.array(data[2].data.field(1))
trigtime = data[0].header["TRIGTIME"]
t = np.array(t-trigtime)
a = -100
b = 300
t1 = 0
t2 = 10
dt = 1
bins = np.arange(a,b+dt,dt)
a2 = []
for i in range(128):
	j = np.where(E==i)
	k = t[j]
	bin_n,bin_edges = np.histogram(k,bins=bins)
	bin_c = (bin_edges[1:]+bin_edges[:-1])*0.5
	#plt.plot(bin_c,bin_n/dt)#,'b')
	tc,cs,bs = TD_baseline(bin_c,bin_n/dt)
	#print(cs)
	index_ = np.where((tc>=t1)&(tc<=t2))[0]
	#index_1 = index_[0]
	#index_2 = index_[-1]
	y = np.mean(cs[index_])
	#print(y)
	a2.append(y)
plt.xlabel('Energy')
plt.ylabel('Count rate')
plt.xscale("log")
plt.yscale("log")
n,m = x1[:-1],a2[:-1]
plt.scatter(n,m,label = "t ={}-{}".format(t1,t2))
plt.plot(n,m,label = "t ={}-{}".format(t1,t2))
plt.legend()
plt.grid()
plt.savefig('spectrum_log.jpg')
#plt.show()
A = np.vstack([n**0,n**1,n**2,n**3,n**4])#n的幂次方矩阵
sol,r,rank,sv = la.lstsq(A.T,m) #最小二乘法拟合，sol返回四个待定系数的值
print(sol[4])
a = float("%.4f" %sol[0])
b = float("%.4f" %sol[1])
c = float("%.4f" %sol[2])
d = float("%.4f" %sol[3])
e = float("%.4f" %sol[4])
y_fit = sol[0] + sol[1]*n + sol[2]*n**2 + sol[3]*n**3 + sol[4]*n**4
plt.plot(n, y_fit, 'b', lw=2, label="{} + {} x+ {} x**2 + {} x**3+ {} x**4".format(a,b,c,d,e))
plt.legend(loc="lower left")
plt.savefig('spectrum_fitting_log.jpg')
plt.show()
