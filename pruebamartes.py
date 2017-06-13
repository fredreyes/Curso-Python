import random


A = []
for x in range(5):
    A.append(random.randint(0,100))
    #if ((A[x]%2)==0):
     #   A.sort(reverse=True)
    #elif((A[x]%2)==1):
    	#A.sort(reverse=False)
    A.sort()

P = []
for x in range(5):
	P.append(random.randint(0,100))
	if x%2==0:
	    P.sort()



Q =[]
for x in range(10):
	Q.append(random.randint(0,100))
zipped = zip(Q[0::2], Q[1::2]) 






if __name__ =='__main__':
	#print(xs[0])
	#printlen(xs))
	print(Q)
	#print(listaPar)
	#print('Suma' , sum(A))