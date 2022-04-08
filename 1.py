import numpy as np
import scipy as sc
import random
import matplotlib.pyplot as plt

n = 10
l = 0.5
m = int(np.log2(n) + 1)
y = []
for i in range(n):
       x = random.random()
       y.append(-np.log(1-x)/l)
y.sort()
t = 0
tau = [0]
for i in range(n):
       t += y[i]
       tau.append(t)

print(np.around(y, decimals = 4))

# m-method with equal interval

yn = y[n-1] - y[0]
j = 0
lenx = [0]*(m+1)
leny = [i*yn/m for i in range(m+1)]
for i in range(m+1):
       while y[j] < leny[i]:
              j+=1
              lenx[i]+=1 #считаем сколько попало в интервал для эмпирической функции распред
lenf = [0]*(m+1)
for i in range(m):
       lenf[i]=lenx[i]/(n*(leny[i+1]-leny[i]))#нормируешь
print(m, np.around(lenf, decimals = 4), np.around(leny, decimals = 4))
lenY = [0]*(1001)#эьто есть эмпирическая
lenX = [i*y[n-1]/1000 for i in range(1001)]#это интервалы для теореетич
lenanY = [l*np.exp(-l*i) for i in lenX]#теоретическая функция распределнеи построение с параметром лямда
k = 0
i = 0
j = 0
for i,j in zip(leny, lenf):
       while lenX[k] < i:
              lenY[k] = j
              k+=1#считаме lenX, чтобы вывести эмпирическую

plt.plot(lenX, lenY, '-')
plt.plot(lenX, lenanY, '-')
plt.show()

#

m0 = 1/l
mm = sum(y)/n
print('M: ', abs(m - mm)*100/m, '%')

d = 1/l**2
dd = 0
for i in y:
       dd += (i - mm)**2
dd /= n
print('D: ', abs(d - dd)*100/d, '%')

x0 = 0.5
def F0(x0):
       return 1 - np.exp(-l*x0)
def Func(RO,r):
       return 1
F = 1 - np.exp(-l*x0)
mu = 0
for i in y:
       if (i <= x0): mu+=1
FF = mu/n
print('F: ', abs(F - FF), '%')

plt.plot(tau, [0]*(n+1), 'o-')
plt.show()

p=[]
r=m-1
R0=0
for i in range(len(leny)):
       p.append(F0(leny[i+1])-F0(leny[i]))

for i in range(m):
       R0+=((lenx[i]-m*p[i])/(m*p[i]))

a=input('Введите параметр Альфа:')#параметр альфа для отвержения гипотез
chi2.ppf(a-1,r)
