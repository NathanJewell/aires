import math
import numpy as np
#angle = input("Angle in radians: ")
#velocityI = input("Velocity in m/s: ")
#measDist = input("Enter measured distance: ")
#dt = input("Enter timestep: ")
angle = .73 
velocityI = 36.5 
measDist = 105 
dt = .001
print("Running with \n  theta=" + str(angle) + "\n  vi=" + str(velocityI) + "\n  maxdist=" + str(measDist) + "\n  dt=" + str(dt))

g = 9.81
theoDist = (velocityI * velocityI * math.sin(2 * angle))/g
print("Theoretical Max: " + str(theoDist))
vix = math.cos(angle)*velocityI
viy = math.sin(angle)*velocityI

kmin = 0
kmax = .00000002
kstep = .00000000001
karr = np.arange(kmin, kmax, kstep)#[x / factor for x in range(minpow, maxpow, precision)]
resarr = []
for i in range(len(karr)):
	k = karr[i]
	print("K is: " + repr(k))
	vxOLD = vix
	vyOLD = viy

	ax = 0
	ay=0
	vxNEW=0
	vyNEW=0
	dyOLD= 0.0001
	dxOLD=0
	dxNEW=0
	dyNEW=0


	ttot = 0
	while (dyOLD > 0.0):
		ax = -1 * k * vxOLD * vxOLD
		ay = (-1 *( k * vyOLD * vyOLD)) - g
		#print("AX %s AY %s" % (repr(ax), repr(ay)))
		vxNEW = vxOLD + ax*dt
		vyNEW = vyOLD + ay*dt
		#print("VX %s VY %s" % (repr(vxNEW), repr(vyNEW)))
		dxNEW = dxOLD + vxNEW*dt + ax*dt*dt
		dyNEW = dyOLD + dyNEW*dt + ay*dt*dt
		#print("DX %s DY %s" % (repr(dxNEW), repr(dyNEW)))
		vxOLD = vxNEW
		vyOLD = vyNEW
		dxOLD = dxNEW
		dyOLD = dyNEW
		ttot += dt
		print("TIME: %s" % repr(ttot))
		
	#print("X distance: %s" % repr(dxOLD))
	#print("Y distance: %s" % repr(dyOLD))
	resarr.append(dxOLD)
print(resarr)
