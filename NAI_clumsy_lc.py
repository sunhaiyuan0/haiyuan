# for NAI_detector to show the light curve of daily data
#====================================================
#set time
#example :date = "201009" #year = 20 ,month = 10 ,date = 09
date = "201009"

#====================================================
#24h_lightcurve
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from Baseline import TD_baseline

catalog = list(range(0,24))
#detector = [0,1]
detector = [0,1,2,3,4,5,6,7,8,9,"a","b"]

plt.figure(figsize=(20,10))
plt.suptitle('0-24h',fontsize = 30,backgroundcolor = "c")
count = 0
dt = 1
for j in detector:
	count += 1
	plt.subplot(6,2,count)
	for i in catalog:
		if i >=10:
			i = str(i)
		else:
			i = str(0)+str(i)
		data = fits.open("glg_tte_n{x}_{z}_{y}z_v00.fit".format(x=j,z=date,y=i))
		t = data[2].data.field(0)
		tstart = data[3].data.field(0)[0]
		tstop = data[3].data.field(1)[-1]
		bins = np.arange(tstart,tstop,dt)
		bin_n ,bin_edges = np.histogram(t,bins=bins)
		bin_c = (bin_edges[1:]+bin_edges[:-1])*0.5
		tc,cs,bs = TD_baseline(bin_c,bin_n/dt)
		plt.plot(tc,bs,color = "r")
		plt.grid()
		plt.ylabel("count/sec")
		plt.xlabel("time")
		if int(i) >=23:
			plt.plot(bin_c,bin_n/dt,color='b',label = "n{x}".format(x=j))
			plt.legend(loc = "upper right")
		else:
			plt.plot(bin_c,bin_n/dt,color='b')
plt.savefig('NAI_24H.png')
plt.show()

#=======================================================
#0-3h_lightcurve
catalog = ["00","01","02"]
detector = [0,1,2,3,4,5,6,7,8,9,'a','b']
plt.figure(figsize=(20,10))
count = 0
plt.suptitle("0-3h",fontsize = 30,backgroundcolor = "c")
#count1 = 0
dt = 1
for j in detector:
	count += 1
	plt.subplot(6,2,count)
	for i in catalog:
		data = fits.open("glg_tte_n{x}_{z}_{y}z_v00.fit".format(x=j,z=date,y=i))
		t = data[2].data.field(0)
		tstart = data[3].data.field(0)[0]
		tstop = data[3].data.field(1)[-1]
		bins = np.arange(tstart,tstop,dt)
		bin_n ,bin_edges = np.histogram(t,bins=bins)
		bin_c = (bin_edges[1:]+bin_edges[:-1])*0.5
		tc,cs,bs = TD_baseline(bin_c,bin_n/dt)
		plt.plot(tc,bs,color='r')
		plt.grid()
		plt.xlabel("time")
		plt.ylabel('count/sec')
		if int(i)%3>=2:
			plt.plot(bin_c,bin_n/dt,color = "b",label = "n{x}".format(x = j))
			plt.legend(loc = "upper right")
		else:
			plt.plot(bin_c,bin_n/dt,color = "b")
tlabel = int(catalog[-1])+1
tlabel1 = tlabel - 3

plt.savefig("NAI_{x}-{y}h".format(x=tlabel1,y=tlabel))

#========================================================
#4-6h_lightcurve
catalog = ["03","04","05"]
detector = [0,1,2,3,4,5,6,7,8,9,'a','b']
plt.figure(figsize=(20,10))
count = 0
plt.suptitle("4-6h",fontsize = 30,backgroundcolor = "c")
#count1 = 0
dt = 1

for j in detector:
	count += 1
	plt.subplot(6,2,count)
	for i in catalog:
		data = fits.open("glg_tte_n{x}_{z}_{y}z_v00.fit".format(x=j,z=date,y=i))
		t = data[2].data.field(0)
		tstart = data[3].data.field(0)[0]
		tstop = data[3].data.field(1)[-1]
		bins = np.arange(tstart,tstop,dt)
		bin_n ,bin_edges = np.histogram(t,bins=bins)
		bin_c = (bin_edges[1:]+bin_edges[:-1])*0.5
		tc,cs,bs = TD_baseline(bin_c,bin_n/dt)
		plt.plot(tc,bs,color='r')
		plt.grid()
		plt.xlabel("time")
		plt.ylabel('count/sec')
		if int(i)%3>=2:
			plt.plot(bin_c,bin_n/dt,color = "b",label = "n{x}".format(x = j))
			plt.legend(loc = "upper right")
		else:
			plt.plot(bin_c,bin_n/dt,color = "b")
tlabel = int(catalog[-1])+1
tlabel1 = tlabel - 3
plt.savefig("NAI_{x}-{y}h".format(x=tlabel1,y=tlabel))

#========================================================
#7-9h_lightcurve
catalog = ["06","07","08"]
detector = [0,1,2,3,4,5,6,7,8,9,'a','b']
plt.figure(figsize=(20,10))
count = 0
plt.suptitle("7-9h",fontsize = 30,backgroundcolor = "c")
dt = 1

for j in detector:
	count += 1
	plt.subplot(6,2,count)
	for i in catalog:
		data = fits.open("glg_tte_n{x}_{z}_{y}z_v00.fit".format(x=j,z=date,y=i))
		t = data[2].data.field(0)
		tstart = data[3].data.field(0)[0]
		tstop = data[3].data.field(1)[-1]
		bins = np.arange(tstart,tstop,dt)
		bin_n ,bin_edges = np.histogram(t,bins=bins)
		bin_c = (bin_edges[1:]+bin_edges[:-1])*0.5
		tc,cs,bs = TD_baseline(bin_c,bin_n/dt)
		plt.plot(tc,bs,color='r')
		plt.grid()
		plt.xlabel("time")
		plt.ylabel('count/sec')
		if int(i)%3>=2:
			plt.plot(bin_c,bin_n/dt,color = "b",label = "n{x}".format(x = j))
			plt.legend(loc = "upper right")
		else:
			plt.plot(bin_c,bin_n/dt,color = "b")
tlabel = int(catalog[-1])+1
tlabel1 = tlabel - 3
plt.savefig("NAI_{x}-{y}h".format(x=tlabel1,y=tlabel))

#========================================================
#10-12h_lightcurve
catalog = ["09","10","11"]
detector = [0,1,2,3,4,5,6,7,8,9,"a",'b']
plt.figure(figsize=(20,10))
count = 0
plt.suptitle("10-12h",fontsize = 30,backgroundcolor = "c")
dt = 1

for j in detector:
	count += 1
	plt.subplot(6,2,count)
	for i in catalog:
		data = fits.open("glg_tte_n{x}_{z}_{y}z_v00.fit".format(x=j,z=date,y=i))
		t = data[2].data.field(0)
		tstart = data[3].data.field(0)[0]
		tstop = data[3].data.field(1)[-1]
		bins = np.arange(tstart,tstop,dt)
		bin_n ,bin_edges = np.histogram(t,bins=bins)
		bin_c = (bin_edges[1:]+bin_edges[:-1])*0.5
		tc,cs,bs = TD_baseline(bin_c,bin_n/dt)
		plt.plot(tc,bs,color='r')
		plt.grid()
		plt.xlabel("time")
		plt.ylabel('count/sec')
		if int(i)%3>=2:
			plt.plot(bin_c,bin_n/dt,color = "b",label = "n{x}".format(x = j))
			plt.legend(loc = "upper right")
		else:
			plt.plot(bin_c,bin_n/dt,color = "b")
tlabel = int(catalog[-1])+1
tlabel1 = tlabel - 3
plt.savefig("NAI_{x}-{y}h".format(x=tlabel1,y=tlabel))

#========================================================
#13-15h_lightcurve
catalog = ["12","13","14"]
detector = [0,1,2,3,4,5,6,7,8,9,"a","b"]
plt.figure(figsize=(20,10))
count = 0
plt.suptitle("13-15h",fontsize = 30,backgroundcolor = "c")
dt = 1

for j in detector:
	count += 1
	plt.subplot(6,2,count)
	for i in catalog:
		data = fits.open("glg_tte_n{x}_{z}_{y}z_v00.fit".format(x=j,z=date,y=i))
		t = data[2].data.field(0)
		tstart = data[3].data.field(0)[0]
		tstop = data[3].data.field(1)[-1]
		bins = np.arange(tstart,tstop,dt)
		bin_n ,bin_edges = np.histogram(t,bins=bins)
		bin_c = (bin_edges[1:]+bin_edges[:-1])*0.5
		tc,cs,bs = TD_baseline(bin_c,bin_n/dt)
		plt.plot(tc,bs,color='r')
		plt.grid()
		plt.xlabel("time")
		plt.ylabel('count/sec')
		if int(i)%3>=2:
			plt.plot(bin_c,bin_n/dt,color = "b",label = "n{x}".format(x = j))
			plt.legend(loc = "upper right")
		else:
			plt.plot(bin_c,bin_n/dt,color = "b")
tlabel = int(catalog[-1])+1
tlabel1 = tlabel - 3
plt.savefig("NAI_{x}-{y}h".format(x=tlabel1,y=tlabel))
#========================================================
#16-18h_lightcurve
catalog = ["15","16","17"]
detector = [0,1,2,3,4,5,6,7,8,9,"a","b"]
plt.figure(figsize=(20,10))
count = 0
plt.suptitle("16-18h",fontsize = 30,backgroundcolor = "c")
dt = 1

for j in detector:
	count += 1
	plt.subplot(6,2,count)
	for i in catalog:
		data = fits.open("glg_tte_n{x}_{z}_{y}z_v00.fit".format(x=j,z=date,y=i))
		t = data[2].data.field(0)
		tstart = data[3].data.field(0)[0]
		tstop = data[3].data.field(1)[-1]
		bins = np.arange(tstart,tstop,dt)
		bin_n ,bin_edges = np.histogram(t,bins=bins)
		bin_c = (bin_edges[1:]+bin_edges[:-1])*0.5
		tc,cs,bs = TD_baseline(bin_c,bin_n/dt)
		plt.plot(tc,bs,color='r')
		plt.grid()
		plt.xlabel("time")
		plt.ylabel('count/sec')
		if int(i)%3>=2:
			plt.plot(bin_c,bin_n/dt,color = "b",label = "n{x}".format(x = j))
			plt.legend(loc = "upper right")
		else:
			plt.plot(bin_c,bin_n/dt,color = "b")
tlabel = int(catalog[-1])+1
tlabel1 = tlabel - 3
plt.savefig("NAI_{x}-{y}h".format(x=tlabel1,y=tlabel))
#========================================================
#18-21h_lightcurve
catalog = ["18","19","20"]
detector = [0,1,2,3,4,5,6,7,8,9,"a","b"]
plt.figure(figsize=(20,10))
count = 0
plt.suptitle("18-21h",fontsize = 30,backgroundcolor = "c")
dt = 1

for j in detector:
	count += 1
	plt.subplot(6,2,count)
	for i in catalog:
		data = fits.open("glg_tte_n{x}_{z}_{y}z_v00.fit".format(x=j,z=date,y=i))
		t = data[2].data.field(0)
		tstart = data[3].data.field(0)[0]
		tstop = data[3].data.field(1)[-1]
		bins = np.arange(tstart,tstop,dt)
		bin_n ,bin_edges = np.histogram(t,bins=bins)
		bin_c = (bin_edges[1:]+bin_edges[:-1])*0.5
		tc,cs,bs = TD_baseline(bin_c,bin_n/dt)
		plt.plot(tc,bs,color='r')
		plt.grid()
		plt.xlabel("time")
		plt.ylabel('count/sec')
		if int(i)%3>=2:
			plt.plot(bin_c,bin_n/dt,color = "b",label = "n{x}".format(x = j))
			plt.legend(loc = "upper right")
		else:
			plt.plot(bin_c,bin_n/dt,color = "b")
tlabel = int(catalog[-1])+1
tlabel1 = tlabel - 3
plt.savefig("NAI_{x}-{y}h".format(x=tlabel1,y=tlabel))
#========================================================
#21-24h_lightcurve
catalog = ["21","22","23"]
detector = [0,1,2,3,4,5,6,7,8,9,"a","b"]
plt.figure(figsize=(20,10))
count = 0
plt.suptitle("21-24h",fontsize = 30,backgroundcolor = "c")
dt = 1

for j in detector:
	count += 1
	plt.subplot(6,2,count)
	for i in catalog:
		data = fits.open("glg_tte_n{x}_{z}_{y}z_v00.fit".format(x=j,z=date,y=i))
		t = data[2].data.field(0)
		tstart = data[3].data.field(0)[0]
		tstop = data[3].data.field(1)[-1]
		bins = np.arange(tstart,tstop,dt)
		bin_n ,bin_edges = np.histogram(t,bins=bins)
		bin_c = (bin_edges[1:]+bin_edges[:-1])*0.5
		tc,cs,bs = TD_baseline(bin_c,bin_n/dt)
		plt.plot(tc,bs,color='r')
		plt.grid()
		plt.xlabel("time")
		plt.ylabel('count/sec')
		if int(i)%3>=2:
			plt.plot(bin_c,bin_n/dt,color = "b",label = "n{x}".format(x = j))
			plt.legend(loc = "upper right")
		else:
			plt.plot(bin_c,bin_n/dt,color = "b")
tlabel = int(catalog[-1])+1
tlabel1 = tlabel - 3
plt.savefig("NAI_{x}-{y}h".format(x=tlabel1,y=tlabel))
