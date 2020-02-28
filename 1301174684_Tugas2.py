# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:07:18 2020

@author: ASUS
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:52:38 2020

@author: ASUS
"""

import matplotlib.pyplot as plt
import pandas as pd
import random as rand
import math

#Nomor 1
data = pd.read_csv("jain.csv")
x = data['x-axis']
y = data['y-axis'] 

# Define plot space
fig, (ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10) = plt.subplots(10, 1, figsize=(6,45))
#visualisasi data set
plt.xlabel('x-labels')
plt.ylabel('y-labels')
ax1.scatter(x,y, color='yellow')
ax1.set(title="Visualisasi Data Set")

#Nomer2
#inisiasi array 2 dimensi centroid(x,y) awal
centroid1 = [[rand.uniform(min(x), max(x)),rand.uniform(min(y), max(y))]]
centroid2 = [[rand.uniform(min(x), max(x)),rand.uniform(min(y), max(y))]]

#inisiasi centroid
ax2.scatter(x,y, color='yellow')
ax2.scatter(centroid1[0][0],centroid1[0][1],color='red')
ax2.scatter(centroid2[0][0],centroid2[0][1],color='blue')
ax2.set(title="Centroid Awal")

jarak_centroid1 = []
jarak_centroid2 = []
bagian_centroid1 = []
bagian_centroid2 = []
SSE_centroid1 = []
SSE_centroid2 = []
jmlsse1 = []
jmlsse2 = []

def jarak(x,cx,y,cy):
    j = math.sqrt(pow(x-cx,2) + pow(y-cy,2))
    return j

def sse(x,cx,y,cy):
    s = pow(x-cx,2) + pow(y-cy,2)
    return s

def rata2_centroid1(dt):
    rata2 = []
    jumlahx = 0
    jumlahy = 0
    for i in range(len(dt)):
        jumlahx = jumlahx + dt[i][0]
        jumlahy = jumlahy + dt[i][1]
    ratax = jumlahx/len(dt)
    ratay = jumlahy/len(dt)
    rata2.append(ratax)
    rata2.append(ratay)
    centroid1.append(rata2)
    
def rata2_centroid2(dt):
    rata2 = []
    jumlahx = 0
    jumlahy = 0
    for i in range(len(dt)):
        jumlahx = jumlahx + dt[i][0]
        jumlahy = jumlahy + dt[i][1]
    
    ratax = jumlahx/len(dt)
    ratay = jumlahy/len(dt)
    rata2.append(ratax)
    rata2.append(ratay)
    centroid2.append(rata2)

def reset_array():
    jarak_centroid1[:] = []
    jarak_centroid2[:] = []
    bagian_centroid1[:] = []
    bagian_centroid2[:] = []
    SSE_centroid1[:] = []
    SSE_centroid2[:] = []

def pindah_centroid():
    reset_array()
    for i in range(len(x)):
        bag = []
        jarak_centroid1.append(jarak(x[i],centroid1[-1][0],y[i],centroid1[-1][1]))
        jarak_centroid2.append(jarak(x[i],centroid2[-1][0],y[i],centroid2[-1][1]))
        SSE_centroid1.append(sse(x[i],centroid1[-1][0],y[i],centroid1[-1][1]))
        SSE_centroid2.append(sse(x[i],centroid2[-1][0],y[i],centroid2[-1][1]))
        if(jarak_centroid1[i] > jarak_centroid2[i]):
            bag.append(x[i])
            bag.append(y[i])
            bagian_centroid2.append(bag)
        else:
            bag.append(x[i])
            bag.append(y[i])
            bagian_centroid1.append(bag)
            

def centroid_akhir():
    #iterasi 1
    pindah_centroid()
    rata2_centroid1(bagian_centroid1)
    rata2_centroid2(bagian_centroid2)
    jmlsse1.append(sum(SSE_centroid1))
    jmlsse2.append(sum(SSE_centroid2))
    while (centroid1[-1] != centroid1[-2]):
        pindah_centroid()
        rata2_centroid1(bagian_centroid1)
        rata2_centroid2(bagian_centroid2)
        jmlsse1.append(sum(SSE_centroid1))
        jmlsse2.append(sum(SSE_centroid2))

#run program
centroid_akhir()
ax3.scatter(x,y, color='yellow')
ax3.scatter(centroid1[-1][0],centroid1[-1][1],color='red')
ax3.scatter(centroid2[-1][0],centroid2[-1][1],color='blue')
ax3.set(title="Centroid Terakhir Bagian A")

#Grafik SSE
k = []
for i in range(len(jmlsse1)):
    k.append(i)
ax4.set(title="SSE Centroid 1")
ax4.plot(k,jmlsse1, 'g--d')

j=[]
for i in range(len(jmlsse2)):
    j.append(i)
ax5.plot(j,jmlsse2, 'g--d')
ax5.set(title="SSE Centroid 2")

###############################

#poin d - h
kelas = data['class']
bag1x = []
bag1y = []
bag2x = []
bag2y = []
bag1 = []
bag2 = []

#visualisasi data berdasarkan kelasnya
for i in range(len(kelas)):
    arr = []
    if (kelas[i] == 1):
        bag1x.append(x[i])
        bag1y.append(y[i])
        arr.append(bag1x[-1])
        arr.append(bag1y[-1])
        bag1.append(arr)
    else:
        bag2x.append(x[i])
        bag2y.append(y[i])
        arr.append(bag2x[-1])
        arr.append(bag2y[-1])
        bag2.append(arr)

centroidbag1 = [[rand.uniform(min(bag1x),max(bag1x)),rand.uniform(min(bag1y),max(bag1y))]]
centroidbag2 = [[rand.uniform(min(bag2x),max(bag2x)),rand.uniform(min(bag2y),max(bag2y))]]

#Grafik Awal
ax6.scatter(bag1x,bag1y,color="blue")
ax6.scatter(bag2x,bag2y,color="red")
ax6.set(title="Visualisasi Data Set Berdasarkan Kelas")

#Grafik inisiasi awal centroid
ax7.scatter(bag1x,bag1y,color="blue")
ax7.scatter(bag2x,bag2y,color="red")
ax7.scatter(centroidbag1[0][0],centroidbag1[0][1],color='yellow')
ax7.scatter(centroidbag2[0][0],centroidbag2[0][1],color='green')
ax7.set(title="Inisisasi Centroid Awal")

jarakbag1 = []
jarakbag2 = []
sse_centroidbag1 = []
sse_centroidbag2 = []
jmlssebag1 = []
jmlssebag2 = []

def rata2_centroidbag1(dt):
    rata2 = []
    jumlahx = 0
    jumlahy = 0
    for i in range(len(dt)):
        jumlahx = jumlahx + dt[i][0]
        jumlahy = jumlahy + dt[i][1]
    ratax = jumlahx/len(dt)
    ratay = jumlahy/len(dt)
    rata2.append(ratax)
    rata2.append(ratay)
    centroidbag1.append(rata2)
    
def rata2_centroidbag2(dt):
    rata2 = []
    jumlahx = 0
    jumlahy = 0
    for i in range(len(dt)):
        jumlahx = jumlahx + dt[i][0]
        jumlahy = jumlahy + dt[i][1]
    ratax = jumlahx/len(dt)
    ratay = jumlahy/len(dt)
    rata2.append(ratax)
    rata2.append(ratay)
    centroidbag2.append(rata2)

def pindah_centroid_bag1():
    jarakbag1[:] = []
    sse_centroidbag1[:] = []
#    bag_centroid1[:] = []
    for i in range(len(bag1x)):
        jarakbag1.append(jarak(bag1x[i],centroidbag1[-1][0],bag1y[i],centroidbag1[-1][1]))
        sse_centroidbag1.append(sse(bag1x[i],centroidbag1[-1][0],bag1y[i],centroidbag1[-1][1]))

            
def pindah_centroid_bag2():
    jarakbag2[:] = []
    sse_centroidbag2[:] = []
    for j in range(len(centroidbag2)):
        for i in range(len(bag2x)):
            jarakbag2.append(jarak(bag2x[i],centroidbag2[j][0],bag2y[i],centroidbag2[j][1]))
            sse_centroidbag2.append(sse(bag2x[i],centroidbag2[j][0],bag2y[i],centroidbag2[j][1]))

def centroid_akhir_bag1():
    #iterasi 1
    pindah_centroid_bag1()
    rata2_centroidbag1(bag1)
    jmlssebag1.append(sum(sse_centroidbag1))
    while (centroidbag1[-1] != centroidbag1[-2]):
        pindah_centroid_bag1()
        rata2_centroidbag1(bag1)
        jmlssebag1.append(sum(sse_centroidbag1))
    else:
        jmlssebag1.append(sum(sse_centroidbag1))

def centroid_akhir_bag2():
    #iterasi 1
    pindah_centroid_bag2()
    rata2_centroidbag2(bag2)
    jmlssebag2.append(sum(sse_centroidbag2))
    while (centroidbag2[-1] != centroidbag2[-2]):
        pindah_centroid_bag2()
        rata2_centroidbag2(bag2)
        jmlssebag2.append(sum(sse_centroidbag2))
    else:
        jmlssebag2.append(sum(sse_centroidbag2))

#Run Program
centroid_akhir_bag1()
centroid_akhir_bag2()
#Grafik Data Centroid Akhir
ax8.scatter(bag1x,bag1y,color="blue")
ax8.scatter(bag2x,bag2y,color="red")
ax8.scatter(centroidbag1[-1][0],centroidbag1[-1][1],color='yellow')
ax8.scatter(centroidbag2[-1][0],centroidbag2[-1][1],color='green')
ax8.set(title="Data Centroid Akhir")

#Grafik SSE
l = []
for i in range(len(jmlssebag1)):
    l.append(i)
ax9.set(title="SSE Centroid 1")
ax9.plot(l,jmlssebag1,'g--d')

m = []
for i in range(len(jmlssebag2)):
    m.append(i)
ax10.plot(m,jmlssebag2, 'g--d')
ax10.set(title="SSE Centroid 2")