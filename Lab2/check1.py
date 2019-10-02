import random



def connect(matrix,n,t):
    visited = []
    cc = []
    for i in range(n):
        visited.append(False)
    for v in range(n):
        if visited[v] == False:
            temp = []
            cc.append(util(matrix, temp, v, visited))
    for x in cc:
        if(len(x) >= t):
            return 1
    return 0

def util(matrix,temp,v,visited):
    visited[v] = True
    temp.append(v)

    for i in matrix[v]:
        if visited[i] == False:
            temp = util(matrix, temp, i, visited)
    return temp

def generate(n,p):
    matrix = [[] for i in range(n)];

    #print("There are "+str(n)+" vertices and the probabilty is "+ str(p));
    for x in range(0, n):
        for y in range(x+1,n):
            q = random.random()
            if(q < p):
                print("edge between "+ str(x)+ " and "+ str(y)+ " added (q="+str(q)+ ", p="+str(p)+ ")")

                matrix[y].append(x);
                matrix[x].append(y);

    return matrix;

"""
print("Enter n: ");
n = input();
print("Enter p: ");
p = input();
print("Enter t: ")
t = input();
"""
n = 40
t = 30
x = 0.2
while x < 3.0:
    total = 0
    p = x/float(n)
    for y in range(500):
        graph = generate(n, p)
        total = total + connect(graph,n,t)
    print(str(x) +"," + str(100*(total/500.0))+"%")
    x+=0.2



"""



print("   "),
for i in range(0,n):
    print(str(i) + " "),
print("")
print("   "),
for i in range(0,n):
    print("--"),
print("")
"""
