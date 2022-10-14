r=int(input("enter no.of rows : "))
c=int(input("enter no.of coloumbs : "))

def entry():
    m=[]
    for i in range(r):
        n=[]
        for j in range(c):
            x=int(input("enter element for matrix : "))
            n.append(x)
        m.append(n)
    return m

def display(p):
    for i in range(r):
        for j in range(c):
            print(p[i][j],end=" ")
        print("\t")

def addition():
    for i in range(r):
        for j in range(c):
            print(m1[i][j]+m2[i][j],end=" ")
        print("\t")

def subtraction():
    for i in range(r):
        for j in range(c):
            sub=m1[i][j] - m2[i][j]
            print(sub,end=" ")
        print("\t")

def multiplication():
    fin=[]
    for i in range(r):
        mul=[]
        for j in range(c):
            add = 0
            for k in range(c):
                add+=m1[i][k]*m2[k][j]
            mul.append(add)
        fin.append(mul)
    return fin

def transpose():
    t=[]
    for i in range(r):
        l=[]
        for j in range(c):
            g=m3[j][i]
            l.append(g)
        t.append(l)
    return t

print(" 1) read and display 1st matrix\n 2) read and display 2nd matrix\n 3) addition of 2 matrix\n 4) substration of 2 matrix\n "
      "5) multiplication of matrix\n 6) transpose of matrix")
print("\t")

while(True):
    ch=int(input("enter your choice : "))
    if ch==1:
        print("1st matrix :")
        m1=entry()
        display(m1)
        print("\t")
    if ch==2:
        print("2nd matrix :")
        m2 = entry()
        display(m2)
        print("\t")
    if ch==3:
        print("addition of matrix :")
        addition()
        print("\t")
    if ch==4:
        print("subtraction of matrix :")
        subtraction()
        print("\t")
    if ch==5:
        print("multiplication of matrix :")
        f=multiplication()
        display(f)
        print("\t")
    if ch==6:
        print("enter matrix that you want to transpose :")
        m3 = entry()
        display(m3)
        print("transposed matrix ")
        m4=transpose()
        display(m4)
        print("\t")
