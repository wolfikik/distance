# coding: utf8
import math

def dist(a,b):
    return pow(pow(a[0] - a[1], 2) + pow(b[0] - b[1], 2), 0.5)

def init():
    ar = []
    ardistance = []
    n = int(raw_input("Введите количество координат:"))
    for i in range(n):
        coord = []
        coord.append(int(raw_input("Введите координату "+str(i+1)+".1:")))
        coord.append(int(raw_input("Введите координату "+str(i+1)+".2:")))
        ar.append(coord)
    for i in range(0, len(ar)):
        for j in range(i+1, len(ar)):
            ardistance.append(dist(ar[i], ar[j]))
    ardistance.sort()
    print('Наименьшее расстояние: '+str(int(ardistance[0])))
init()