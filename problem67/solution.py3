array = []
with open('triangle.txt', 'r') as f:
    myarray = [line.split() for line in f]

for k in range(0,99):
    for i in range(0,99-k):
        myarray[99-k-1][i] = int(myarray[99-k-1][i]) + max(int(myarray[99-k][i+1]),int(myarray[99-k][i]))

print myarray[0][0]
