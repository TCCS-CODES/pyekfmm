
## This DEMO is a 3D example [x,y,z] with constant velocity and with one shot
# 
#  COPYRIGHT: Yangkang Chen, 2022, The University of Texas at Austin

import aaspip.ekfmm as fmm
import matplotlib.pyplot as plt
import numpy as np

vel=3.09354*np.ones([101*101*101,1],dtype='float32');
t=fmm.eikonal(vel,xyz=np.array([0.5,0,0]),ax=[0,0.01,101],ay=[0,0.01,101],az=[0,0.01,101],order=2);
time=t.reshape(101,101,101,order='F'); #[x,y,z]

velx=3.80395*np.ones([101*101*101,1],dtype='float32'); #velocity axis must be x,y,z respectively
# velx=3.09354*np.ones([101*101*101,1],dtype='float32'); #velocity axis must be x,y,z respectively

eta=0.340859*np.ones([101*101*101,1],dtype='float32'); #velocity axis must be x,y,z respectively
eta=0.340859*np.ones([101*101*101,1],dtype='float32');
t=fmm.eikonalvti(velx,vel,eta,xyz=np.array([0.5,0,0]),ax=[0,0.01,101],ay=[0,0.01,101],az=[0,0.01,101],order=1);
time2=t.reshape(101,101,101,order='F');#first axis (vertical) is x, second is z


## Verify
print(['Testing result:',time.max(),time.min(),time.std(),time.var()])
print(['Correct result:',0.4845428, 0.0, 0.08635751, 0.00745762])

from aaspip import plot3d
data=np.transpose(time,(2,0,1)); ## data requires [z,x,y], as required by the plot3d function
data2=np.transpose(time2,(2,0,1)); ## data requires [z,x,y], as required by the plot3d function

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(121, projection='3d')
plot3d(data,frames=[0,0,0],cmap=plt.cm.jet,ifnewfig=False,showf=False,close=False,nlevel=10, barlabel='Traveltime (s)');
plt.gca().set_xlabel("X (km)",fontsize='large', fontweight='normal')
plt.gca().set_ylabel("Y (km)",fontsize='large', fontweight='normal')
plt.gca().set_zlabel("Z (km)",fontsize='large', fontweight='normal')
plt.gca().text(-0.124, 0, -0.66, "a)", fontsize=28, color='k')
plt.title('Isotropic',color='k', fontsize=20)

ax = fig.add_subplot(122, projection='3d')
plot3d(data2,frames=[0,0,0],cmap=plt.cm.jet,ifnewfig=False,showf=False,close=False,nlevel=10,barlabel='Traveltime (s)');
plt.gca().set_xlabel("X (km)",fontsize='large', fontweight='normal')
plt.gca().set_ylabel("Y (km)",fontsize='large', fontweight='normal')
plt.gca().set_zlabel("Z (km)",fontsize='large', fontweight='normal')
plt.gca().text(-0.124, 0, -0.66, "b)", fontsize=28, color='k')
plt.title('Anisotropic',color='k', fontsize=20)

plt.savefig('test_aaspip_ekfmm_fig2.png',format='png',dpi=300,bbox_inches='tight', pad_inches=0)
plt.savefig('test_aaspip_ekfmm_fig2.pdf',format='pdf',dpi=300,bbox_inches='tight', pad_inches=0)

plt.show()

