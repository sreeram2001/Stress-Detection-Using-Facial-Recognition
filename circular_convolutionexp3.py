import matplotlib.pyplot as plt
import numpy as np

x1=[]
x2=[]
t=0
r=0
n1=int(input("Enter no. of elements for 1st seq."))
n2=int(input("Enter no. of elements for 2nd seq."))
for i in range(n1):
    r=int(input("Enter for 1st"))
    x1.append(r)
    
h=[]
for i in range(n2):
    r=int(input("Enter for 2nd"))
    h.append(r)
    x2.append(r)
    
if(n1>n2):
    for i in range(n2-1,n1-1,1):
        x2.append(0)
else:
    for i in range(n1-1,n2-1,1):
        x1.append(0)


if(n1>n2):
    N=n1
else:
    N=n2
        
p=np.arange(0,N,1)
plt.subplot(3,3,1)
plt.title("x1")
plt.xlabel("n")
plt.grid("true")
plt.stem(p,x1)

plt.subplot(3,3,2)
plt.title("x2")
plt.xlabel("n")
plt.grid("true")
plt.stem(p,x2)


x3=[]
y=[]
def neg(x,N):
    x3.append(x[0])
    for i in range(N-1,0,-1):
        x3.append(x[i])
    return x3
x6=[]
x5=0
def shift(x,m,N):
    x6=[]
    for i in range(0,N,1):
        x6.append(x[i-m])
    return x6
            

def cir_con(x1,x2):
    t=0
    x4=neg(x2,N)
    for m in range(0,N,1):
        x5=shift(x4,m,N)
        print(x5)
        for j in range(0,N,1):
            t+=x1[j]*x5[j]
        y.append(t)
        t=0
    print(y)

cir_con(x1,x2)

k=np.arange(0,N,1)
k1=np.arange(0,n1+n2-1,1)
plt.subplot(3,3,3)
plt.title("Circular convolution")
plt.xlabel("n")
plt.grid("true")
plt.stem(k,y)



#linear convolution
x=x1
yl=[]
print(x)
print(h)
def lin_con(x,h):
    t=0
    for k in range(0,n1+n2-1,1):
        t=0
        for i in range(0,n1,1):
            for j in range(0,n2,1):
                if((i+j)==k):
                    t+=x[i]*h[j]
        yl.append(t)
    print(yl)
            
lin_con(x,h)

plt.subplot(3,3,4)
plt.title("Linear convolution")
plt.xlabel("n")
plt.grid("true")
plt.stem(k1,yl)

w=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
w_c=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(0,N,1):
    for j in range(0,N,1):
        w[i][j]=(np.exp(-2j*np.pi/N))**(i*j)
        w_c[i][j]=(np.exp(2j*np.pi/N))**(i*j)

for i in range(0,4,1):
    for j in range(0,4,1):       
        print(w[i][j])

xk1=[]
xk2=[]
xk3=[]
for i in range(0,4,1):
    t=0
    for j in range(0,4,1):
        t+=w[i][j]*x1[j]
    xk1.append(t)


p1=np.arange(0,len(xk1),1)

xk11=np.abs(xk1)
plt.subplot(3,3,5)
plt.title("xk1")
plt.xlabel("K")
plt.grid("true")
plt.stem(p1,xk11)


for i in range(0,4,1):
    t=0
    for j in range(0,4,1):
        t+=w[i][j]*x2[j]
    xk2.append(t)
    
xk21=np.abs(xk2)
plt.subplot(3,3,6)
plt.title("xk2")
plt.xlabel("K")
plt.grid("true")
plt.stem(p1,xk21)


print(xk1)
print(xk2)
t=0
for i in range(0,4,1):
    t=xk1[i]*xk2[i]
    xk3.append(t)


xk31=np.abs(xk3)
plt.subplot(3,3,7)
plt.title("xk3=xk1*xk2")
plt.xlabel("K")
plt.grid("true")
plt.stem(p1,xk31)


x3=[]
for i in range(0,4,1):
    t=0
    for j in range(0,4,1):
        t+=w_c[i][j]*xk3[j]
    x3.append(t*0.25)

x31=np.abs(x3)
plt.subplot(3,3,8)
plt.title("x3")
plt.xlabel("n")
plt.grid("true")
plt.stem(p1,x31)
print(x31)
plt.show()