import csv
import copy
import matplotlib.pyplot as plt
from math import cos, cosh, radians
import numpy as np

f = open('analysis.csv', 'r')
reader = csv.DictReader(f)
lista = list(reader)

pts = [] 
etas = []
phis = []
massa = []

for i in range(0, len(lista)):
    pts.append(eval(lista[i]["Tau_pt"]))
    etas.append(eval(lista[i]["Tau_eta"]))
    phis.append(eval(lista[i]["Tau_phi"]))

for i in range(0, len(pts)):
    try:
        massa.append((2*pts[i][0]*pts[i][1]*(cosh((etas[i][0])-(etas[i][1]))-cos((phis[i][0])-(phis[i][1]))))**(1/2))
    except:
        pass

plt.hist(massa, bins = 1000)
plt.xlim(0,150)
plt.show()


#----------------------------------

sorting = copy.deepcopy(pts)
sorting.sort(reverse=True)
print(sorting[0])

pt1 = pts[pts.index(sorting[0])][0]
pt2 = pts[pts.index(sorting[0])][1]
eta1 = etas[pts.index(sorting[0])][0]
eta2 = etas[pts.index(sorting[0])][1]
phi1 = phis[pts.index(sorting[0])][0]
phi2 = phis[pts.index(sorting[0])][1]

Mass = (2*pt1*pt2*(cosh(radians(eta1)-radians(eta2))-cos(radians(phi1)-radians(phi2))))**(1/2)
print(Mass)






