import matplotlib.pyplot as plt
import numpy as np
from math import pi
import os
from time import sleep
import math


res=[]
cap=[]
ind=[]


#reading data
os.system('clear')
print("Entering details of LCR Circuit....")
freq=float(input("Enter the frequency of input : "))
Vmax=float(input("Enter the maximum voltage of input : "))
sleep(1)
os.system('clear')

print("Entering details of lcr circuit.....")
print("Resistance : \n")
res_cnt=int(input("Enter the no of resistors in circuit : "))
for x in range(0,res_cnt,1):
    res_tmp=float(input("Enter resistance R"+str(x+1)+": "))
    res.append(res_tmp)
sleep(1)
os.system('clear')

print("Entering details of LCR Circuit......\n")
print("Inductors :\n")
ind_cnt=int(input("Enter no of inductors in circuit : "))
for x in range(0,ind_cnt,1):
    ind_tmp=float(input("Enter inductance L"+str(x+1)+": "))
    ind.append(ind_tmp)
sleep(1)
os.system('clear')

print("Entering details of lcr circuit.....")
print("Capacitors : \n")
cap_cnt=int(input("Enter the no of capacitors in circuit : "))
for x in range(0,cap_cnt,1):
    cap_tmp=float(input("Enter capacitance C"+str(x+1)+": "))
    cap.append(cap_tmp)
sleep(1)
os.system('clear')



#calculating data
Rnet=sum(res)
Cnet=sum(cap)
Lnet=sum(ind)

afreq=2*math.pi*freq
tper=1/afreq
Vrms=Vmax/math.sqrt(2)
Vavg=Vmax*2/math.pi
if Lnet!=0:
	Xl=afreq*Lnet
else:
	Xl=0
if Cnet!=0:
	Xc=1/(afreq*Cnet)
else:
	Xc=0
Z=math.sqrt(math.pow(Rnet,2)+math.pow(Xc-Xl,2))
if Z==0:
	print("Circuit is short")
	flag=0
else:
	flag=1
	Irms=Vrms/Z
	Imax=math.sqrt(2)*Irms
	Iavg=Imax*2/pi
	ph=math.atan((Xl-Xc)/Rnet)

if(flag==1):
	#Printing values
	print("Net Resistance : Rnet ",str(Rnet))
	print("Net Inductance : Lnet ",str(Lnet))
	print("Net Capacitance Cnet : ",str(Cnet))
	print("Capacitive Impedance Xc : ",str(Xc))
	print("Inductive Impedance Xl : ",str(Xl))
	print("Average Voltage Vavg : ",str(Vavg))
	print("RMS Voltage Vrms : ",str(Vrms))
	print("Average Current Iavg : ",str(Iavg))
	print("RMS Current Irms: ",str(Irms))
	print("Maximum Current Imax: ",str(Imax))
	print("Phase Angle \u03A6: ",str(ph))

	input("Press Enter to view graph......")

	#plotting graph

	n=7.28/afreq
	t=np.arange(0,n,0.0005)

	Vamp=np.sin(afreq*t)*Vmax
	Iamp=np.sin((afreq*t)-ph)*Imax

	plt.plot(t,Vamp)
	plt.plot(t,Iamp)
	plt.legend(["Voltage","Current"],loc="upper right")
	plt.grid()
	plt.ylabel("Volts/Ampere")
	plt.xlabel("time")
	plt.show()

else:
	print("Program Over")
