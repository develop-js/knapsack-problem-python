print('Total Capacity : (kg)')
M = float(input())

print('Count of Weights :')
n = int(input())

print('Enter Weights :')
W=[]
for i in range(0,n):
    temp=int(input())
    W.append(temp)
else :
    print('Enter Values :')
P=[]
for i in range(0,n):
    tem=int(input())
    P.append(tem)

K=[]
for i in range(0,n):
         K = [x/y for x,y in zip(P,W)]

for i in range(0,n):

  for j in range(i+1,n):
  
      if(K[j] > K[i]):
      
          tmp = K[i]
          K[i] = K[j]
          K[j] = tmp

          tmp2 = W[i]
          W[i] = W[j]
          W[j] = tmp2

          tmp3 = P[i]
          P[i] = P[j]
          P[j] = tmp3
      

rc=M
X=[]

for i in range(0,n):
  if(W[i]>rc):
      X.insert(i,0)
      F=X[i]
      
  else:
      X.insert(i,1)
      rc-=W[i]
      F=X[i]

  if(i<n-1 and F==0):
        g=(rc)/(W[i])
        X.insert(i,g)
        (rc)-=((W[i])*(X[i]))
    

sum=0
summ=0
for i in range(0,n):
    sum+=(X[i])*(W[i])

for i in range(0,n):
    summ+=(X[i])*(P[i])



print('********************')
print(' P =', P)
print('********************')
print(' W =', W)
print('********************')
print(' P/W =', K)
print('********************')
print(' X =', X)
print('********************')
print(' X[i] * W[i] =', sum)
print('********************')
print(' X[i] * P[i] =', summ)
print('********************')
print(' M =', M ,",", " n =", n)
print('********************')
ggh = int(input())
