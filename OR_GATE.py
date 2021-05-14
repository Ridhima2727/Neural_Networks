print("----Basic OR GATE implementation------")
#input matrices
x1=[0,0] 
x2=[1,0]
x3=[0,1]
x4=[1,1]
d=[0,1,1,1] #desired output
w1=w2=w3=w4=w5=[] #initializing weights as empty matrix
w1=eval(input("Enter the weight matrix:"))
c=float(input("Enter the learning constant:"))

X=[x1,x2,x3,x4]
W=[w1,w2,w3,w4,w5]

for i in range(4):
    print("w{0} = {1}\nx{2}= {3}".format(i+1,W[i],i+1,X[i]))
    net=X[i][0]*W[i][0]+X[i][1]*W[i][1] #calculating net 
    print("net{0} = {1}".format(i+1,net))
    if net>=0.2:   #output is 1 if the net is greater than the threshold
        out=1
    else:          #output is 0 if the net is greater than the threshold
        out=0
    print("o{0} = {1}".format(i+1,out))
    print("d%s is %s" %(i+1,d[i]))
    if out==d[i]:   #comparing the output with desired output
        print("No weight updation\nw{}=w{}".format(i+1,i+2))
        W[i+1]=W[i]
        print("w{0} is {1}" .format(i+2,W[i+1]))
    else:
        print("Weight updation required")
        a=(c*(d[i]-out))*X[i][0]  #calculation delta W 
        b=(c*(d[i]-out))*X[i][1]  
        W[i+1].append(W[i][0]+a)  #forming an updated new weight matrix
        W[i+1].append(W[i][1]+b)
        print("w {0} is {1}" .format(i+2,W[i+1]))
    print()

print("The final weights are:")
for i in range(len(W)):
    print("W{} = {}".format(i+1,W[i]))